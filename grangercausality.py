import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from pytrends.request import TrendReq
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests

df2020 = pd.read_csv('/home/adudella/PycharmProjects/predictiveModeling/covidCasesKeywords/us-counties-2020.csv')
df2021 = pd.read_csv('/home/adudella/PycharmProjects/predictiveModeling/covidCasesKeywords/us-counties-2021.csv')

combine_df = [df2020, df2021]
df = pd.concat(combine_df)

date_df = pd.DataFrame(df[(df['date'] >= '2020-04-05') & (df['date'] <= '2021-04-03')])
my_us_df = pd.DataFrame(date_df, columns=['date', 'cases'])

my_us_df.sort_values(by=['date'])
cases_sum = 0
prevdate = '2020-04-05'

uscasesbydate = pd.DataFrame(columns=['date', 'casesbydate'])
uscasesbyweek = pd.DataFrame(columns=['weekdate', 'casesbyweek'])


def insert(df, row):
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc + 1] = row


rowdata = []
for index, row in my_us_df.iterrows():
    if (row['date'] == prevdate):
        cases_sum = cases_sum + row['cases']
    else:
        rowdata = []
        rowdata.append(prevdate)
        rowdata.append(str(cases_sum))
        insert(uscasesbydate, rowdata)
        cases_sum = 0
        prevdate = row['date']

prevdate = '2020-04-05'
cases_sum = 0
for index, row in uscasesbydate.iterrows():

    if (index % 7 != 0):
        cases_sum = cases_sum + int(row['casesbydate'])
    else:
        rowdata = []
        rowdata.append(row['date'])
        rowdata.append(cases_sum)
        insert(uscasesbyweek, rowdata)
        cases_sum = 0

df_max_scaled = uscasesbyweek.copy()

# apply normalization techniques (scales it down)
df_max_scaled['casesbyweek'] = (df_max_scaled['casesbyweek'] - df_max_scaled['casesbyweek'].min()) / (
        df_max_scaled['casesbyweek'].max() - df_max_scaled['casesbyweek'].min())

df_max_scaled['casesbyweek'] = round(df_max_scaled['casesbyweek'] * 100)


# print(df_max_scaled['casesbyweek']  )


# GOOGLE TRENDS API PART

def getGoogleArray(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    return df2


def getDataFrame(keyword1, date1, date2):
    df3 = getGoogleArray(keyword1, date1, date2)
    dftimes1 = df3.index.tolist()
    dfkeyword1 = df3[keyword1].tolist()
    time_keyword1 = pd.DataFrame(
        {'Time': dftimes1,
         'ADHD': dfkeyword1,
         })
    return time_keyword1


all_keyworddata = getDataFrame('ADHD', '2020-04-05', '2021-04-03')
time_keyword1 = all_keyworddata


google_trends = time_keyword1['ADHD'].to_frame()

# gets correlation between the casesbyweek (scaled) and other google trends
usCovidData = df_max_scaled['casesbyweek'].to_frame()

google_trends.reset_index(drop=True, inplace=True)
usCovidData.reset_index(drop=True, inplace=True)

usCovidData = usCovidData.astype(int)

rowdata = []
for row1 in google_trends.iterrows():
    rowdata.append(row1[1]['ADHD'])

results = pd.DataFrame()
results['adhd'] = rowdata
rowdata = []
for row1 in usCovidData.iterrows():
    rowdata.append(row1[1]['casesbyweek'])

results['uscases'] = rowdata

print(results.tail(10))


def grangers_causation_matrix(data, variables, test='ssr_chi2test', verbose=False):
    """Check Granger Causality of all possible combinations of the Time series.
    The rows are the response variable, columns are predictors. The values in the table
    are the P-Values. P-Values lesser than the significance level (0.05), implies
    the Null Hypothesis that the coefficients of the corresponding past values is
    zero, that is, the X does not cause Y can be rejected.

    data      : pandas dataframe containing the time series variables
    variables : list containing names of the time series variables.
    """
    maxlag = 12

    df = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
    for c in df.columns:
        for r in df.index:
            test_result = grangercausalitytests(data[[r, c]], maxlag=maxlag, verbose=False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
            min_p_value = np.min(p_values)
            df.loc[r, c] = min_p_value
    df.columns = [var + '_x' for var in variables]
    df.index = [var + '_y' for var in variables]
    return df

print(grangers_causation_matrix(results,['adhd','uscases']))
