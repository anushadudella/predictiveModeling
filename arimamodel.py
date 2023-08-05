import pandas as pd
import plotly.express as px
import pmdarima as pm
import matplotlib.pyplot as plt
import warnings

import Constants

warnings.filterwarnings('ignore')
import pandas as pd
from pytrends.request import TrendReq
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.stattools import adfuller
from loadInput import loadFiles

df = loadFiles()
date_df = pd.DataFrame(df[(df['date'] >= Constants.COVID_START_DATE) & (df['date'] <= Constants.COVID_END_WEEK)])
my_us_df = pd.DataFrame(date_df, columns=['date', 'cases'])

my_us_df.sort_values(by=['date'])
cases_sum = 0
prevdate = Constants.COVID_START_DATE

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

prevdate = Constants.COVID_START_DATE
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
    return df3


all_keyworddata = getDataFrame('ADHD', Constants.COVID_START_DATE, Constants.COVID_END_WEEK)
time_keyword1 = all_keyworddata

time_keyword1 = time_keyword1.drop(['isPartial'], axis=1)
print(time_keyword1.head(15))

usCovidData = df_max_scaled['casesbyweek'].to_frame()
usCovidData = usCovidData.astype(int)

rowdata = []
for row1 in usCovidData.iterrows():
    rowdata.append(row1[1]['casesbyweek'])

time_keyword1['uscases'] = rowdata

# This code  remains for now as it is

final_df=time_keyword1.resample('W').mean()

model = pm.auto_arima(final_df['uscases'],
                        m=20, seasonal=True,
                      start_p=0, start_q=0, max_order=4, test='adf',error_action='ignore',
                           suppress_warnings=True,
                      stepwise=True, trace=True, seasonal_test = 'ch')

train=final_df[(final_df.index.get_level_values(0) >= Constants.COVID_START_DATE) & (final_df.index.get_level_values(0) <= Constants.COVID_END_WEEK_70_PERCENT)]
test=final_df[(final_df.index.get_level_values(0) > Constants.COVID_END_WEEK_70_PERCENT)]


model.fit(train['uscases'])
forecast=model.predict(n_periods=20, return_conf_int=True)

forecast_df = pd.DataFrame(forecast[0],index = test.index,columns=['Prediction'])

pd.concat([final_df['uscases'],forecast_df],axis=1).plot()
plt.savefig(Constants.OUTPUT_LOC + 'USCovidPrediction_ARIMA.jpeg', bbox_inches='tight')

model = pm.auto_arima(final_df['ADHD'],
                        m=12, seasonal=True,
                      start_p=0, start_q=0, max_order=4, test='adf',error_action='ignore',
                           suppress_warnings=True,
                      stepwise=True, trace=True, seasonal_test = 'ch')

train=final_df[(final_df.index.get_level_values(0) >= Constants.COVID_START_DATE) & (final_df.index.get_level_values(0) <= Constants.COVID_END_WEEK_70_PERCENT)]
test=final_df[(final_df.index.get_level_values(0) > Constants.COVID_END_WEEK_70_PERCENT)]

model.fit(train['ADHD'])
forecast=model.predict(n_periods=20, return_conf_int=True)

forecast_df = pd.DataFrame(forecast[0],index = test.index,columns=['Prediction'])

pd.concat([final_df['ADHD'],forecast_df],axis=1).plot()
plt.savefig(Constants.OUTPUT_LOC + 'ADHDPrediction_ARIMA.jpeg', bbox_inches='tight')