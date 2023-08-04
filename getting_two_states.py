import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from pathlib import Path
from sklearn.metrics.pairwise import euclidean_distances
# import seaborn as sns
# import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd
import Constants


# from statsmodels.tsa.stattools import adfuller
# from statsmodels.tsa.seasonal import seasonal_decompose

def getGoogleArray(keyword1, date1, date2, GEOPARAM):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2], geo=GEOPARAM)
    df2 = pytrend.interest_over_time()
    # filepath = Path('/Users/kkaa_austin/PycharmProjects/PredictCovid/' + keyword1
    #                 + '_' + date1 + '_' + date2 + '_' + 'Data.csv')
    # df2.to_csv(filepath)
    return df2

def getDataFrame(keyword1, date1, date2, GEOPARAM):
    df3 = getGoogleArray(keyword1, date1, date2, GEOPARAM)
    dftimes1 = df3.index.tolist()
    dfkeyword1 = df3[keyword1].tolist()
    time_keyword1 = pd.DataFrame(
        {'Time': dftimes1,
         'Keyword': dfkeyword1,
         })
    return time_keyword1

#pre-covid
precovid_keyword1 = getDataFrame('delusions', '2018-04-08', '2019-04-06', 'US-OH')
precovid_keyword2 = getDataFrame('delusions', '2018-04-08', '2019-04-06', 'US-OR')

#during-covid
duringcovid_keyword3 = getDataFrame('delusions', '2020-04-05', '2021-04-03', 'US-OH')
duringcovid_keyword4 = getDataFrame('delusions', '2020-04-05', '2021-04-03', 'US-OR')

time1 = precovid_keyword1.index.tolist()
time1_series = precovid_keyword1.index
precovid1 = precovid_keyword1['Keyword'].tolist()
keyword1_series = precovid_keyword1['Keyword']

time1_keyword1_2018_19 = pd.DataFrame(
    {
     'Ohio': precovid1,
     })

time2 = precovid_keyword2.index.tolist()
precovid2 = precovid_keyword2['Keyword'].tolist()
keyword2_series = precovid_keyword2['Keyword']

time2_keyword2_2020_21 = pd.DataFrame(
    {
     'Oregon': precovid2,
     })

time3 = duringcovid_keyword3.index.tolist()
precovid2 = duringcovid_keyword3['Keyword'].tolist()
keyword3_series = duringcovid_keyword3['Keyword']

time3_keyword2_2020_21 = pd.DataFrame(
    {
     'Ohio': precovid2,
     })

time4 = duringcovid_keyword4.index.tolist()
precovid2 = duringcovid_keyword4['Keyword'].tolist()
keyword4_series = duringcovid_keyword4['Keyword']

time4_keyword2_2020_21 = pd.DataFrame(
    {
     'Oregon': precovid2,
     })

#define subplot layout
fig, axes = plt.subplots(nrows=1, ncols=2)

#add DataFrames to subplots
time1_keyword1_2018_19.plot(ax=axes[0])
time2_keyword2_2020_21.plot(ax=axes[0])
time3_keyword2_2020_21.plot(ax=axes[1])
time4_keyword2_2020_21.plot(ax=axes[1])

axes[0].set_title("Delusions 2018-2019")
axes[0].set_xlabel('Months')
axes[0].set_xticklabels(['blank','April','June','August', 'November', 'January', 'March'])
axes[0].set_ylabel('Google Search Frequency')

axes[1].set_title("Delusions 2020-2021")
axes[1].set_xlabel('Months')
axes[1].set_xticklabels(['blank','April','June','August', 'November', 'January', 'March'])
axes[1].set_ylabel('Google Search Frequency')

axes[0].legend(loc='upper left')
axes[1].legend(loc='upper left')

plt.savefig(Constants.OUTPUT_LOC + 'getTwoStates.jpeg', bbox_inches='tight')

