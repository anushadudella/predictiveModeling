import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import pandas as pd
import Constants

def getGoogleArray(keyword1, date1, date2, GEOPARAM):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2], geo=GEOPARAM)
    df2 = pytrend.interest_over_time()
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

time_keyword1 = getDataFrame('anxiety','2018-04-04','2019-04-06', 'US-OH')
time_keyword2 = getDataFrame('anxiety','2020-04-05','2021-04-06', 'US-OH')

time1 = time_keyword1.index.tolist()
keyword1 = time_keyword1['Keyword'].tolist()
time1_keyword1_2018_19 = pd.DataFrame(
    {'Time': time1,
     'anxiety 2018-2019 US-OH': keyword1,
    })

time2 = time_keyword2.index.tolist()
keyword2 = time_keyword2['Keyword'].tolist()
time2_keyword2_2020_21 = pd.DataFrame(
    {'Time': time2,
     'anxiety 2020-2021 US-OH': keyword2,
    })

ax = time1_keyword1_2018_19.plot(x='Time', y='anxiety 2018-2019 US-OH')
time2_keyword2_2020_21.plot(ax=ax, x='Time', y='anxiety 2020-2021 US-OH')

plt.xlabel('Time in Weeks')
plt.ylabel('Freq. of Keywords')
plt.legend(loc='upper left')
plt.savefig(Constants.OUTPUT_LOC + 'twoRegionEuclidDist.jpeg', bbox_inches='tight')
