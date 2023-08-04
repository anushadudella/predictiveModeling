import pandas as pd
from pytrends.request import TrendReq
import numpy
import matplotlib.pyplot as plt

df2020 = pd.read_csv('us-counties-2020.csv')
df2021 = pd.read_csv('us-counties-2021.csv')

combine_df = [df2020,df2021]
df = pd.concat(combine_df)

date_df = pd.DataFrame(df[(df['date'] >= '2020-04-05') & (df['date'] <= '2021-04-03')])
#april_df = pd.DataFrame(date_df[date_df['state'] == 'Oregon'])
my_us_df = pd.DataFrame(date_df, columns = ['date','cases'])

my_us_df.sort_values(by=['date'])
cases_sum = 0
prevdate = '2020-04-05'

uscasesbydate = pd.DataFrame(columns = ['date', 'casesbydate'])
uscasesbyweek = pd.DataFrame(columns = ['weekdate', 'casesbyweek'])

def insert(df, row):
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc + 1] = row

rowdata = []
for index,row in my_us_df.iterrows():
    if(row['date'] == prevdate):
        cases_sum = cases_sum + row['cases']
    else:
        rowdata = []
        rowdata.append(prevdate)
        rowdata.append(str(cases_sum))
        insert(uscasesbydate,rowdata)
        cases_sum = 0
        prevdate = row['date']

prevdate = '2020-04-05'
cases_sum = 0
for index,row in uscasesbydate.iterrows():

    if(index % 7 != 0):
        cases_sum = cases_sum + int(row['casesbydate'])
    else:
        rowdata = []
        rowdata.append(row['date'])
        rowdata.append(cases_sum)
        insert(uscasesbyweek,rowdata)
        cases_sum = 0

df_max_scaled = uscasesbyweek.copy()
print(df_max_scaled.head(10))

# apply normalization techniques (scales it down)
df_max_scaled['casesbyweek'] = (df_max_scaled['casesbyweek'] - df_max_scaled['casesbyweek'].min()) / (
                df_max_scaled['casesbyweek'].max() - df_max_scaled['casesbyweek'].min())

# df_max_scaled['casesbyweek'] = df_max_scaled['casesbyweek'] / df_max_scaled['casesbyweek'].abs().max()
#
# df_max_scaled['casesbyweek'] = (df_max_scaled['casesbyweek'] -
#                        df_max_scaled['casesbyweek'].mean()) / df_max_scaled['casesbyweek'].std()

df_max_scaled['casesbyweek']  = round(df_max_scaled['casesbyweek'] * 100)

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


all_keyworddata= getDataFrame('ADHD','2020-04-05', '2021-04-03')
time_keyword1 = all_keyworddata #pd.DataFrame(all_keyworddata[all_keyworddata['Time'] <= '2020-12-27'])

# print(time_keyword1)
google_trends = time_keyword1['ADHD'].to_list()
print(google_trends)

# gets correlation between the casesbyweek (scaled) and other google trends
usCovidData = df_max_scaled['casesbyweek'].to_list()
print(usCovidData)
print(str(numpy.corrcoef(google_trends,usCovidData)))

plt.scatter(usCovidData, google_trends , label='scatterplot')
plt.legend(loc='best', fontsize=16)
plt.xlabel('COVID-19')
plt.ylabel('ADHD')
plt.show()