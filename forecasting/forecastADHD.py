import pandas as pd
import plotly.express as px
import pmdarima as pm

import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from pytrends.request import TrendReq
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.stattools import adfuller

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

# GOOGLE TRENDS API PART

def getGoogleArray(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    return df2


def getDataFrame(keyword1, date1, date2):
    df3 = getGoogleArray(keyword1, date1, date2)
    print(df3.head(10))
    exit(0)
    dftimes1 = df3.index.tolist()
    dfkeyword1 = df3[keyword1].tolist()
    time_keyword1 = pd.DataFrame(
        {'Time': dftimes1,
         'ADHD': dfkeyword1,
         })
    return time_keyword1


all_keyworddata = getDataFrame('ADHD', '2020-04-05', '2021-04-03')
time_keyword1 = all_keyworddata

print(time_keyword1.head(10))
print(df_max_scaled.head(10))

exit(0)

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


df['timeStamp']=pd.to_datetime(df['timeStamp'])
fig = px.line(df, x='timeStamp', y='demand', title='Energy Consumption')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(step="all")
        ])
    )
)
#fig.show()

el_df=df.set_index('timeStamp')
#el_df.plot(subplots=True)

#impute missing values

df['demand']=df['demand'].fillna(method='ffill')
df['temp']=df['temp'].fillna(method='ffill')
df['temp']=df['precip'].fillna(method='ffill')

#aggregate values

el_df.resample('M').mean()

#replot the values

#el_df.resample('M').mean().plot(subplots=

#resampled dataset

final_df=el_df.resample('M').mean()

print(final_df.head(10))