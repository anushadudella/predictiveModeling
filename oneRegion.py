import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from pathlib import Path
from sklearn.metrics.pairwise import euclidean_distances

import pandas as pd
import Constants


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
         'Keyword': dfkeyword1,
         })
    return time_keyword1


time_keyword1 = getDataFrame('anxiety', '2018-04-04', '2019-04-06')
time_keyword2 = getDataFrame('anxiety', '2020-04-05', '2021-04-06')

time1 = time_keyword1.index.tolist()
keyword1 = time_keyword1['Keyword'].tolist()
time1_keyword1_2018_19 = pd.DataFrame(
    {'Time': time1,
     '2018-2019': keyword1,
     })

time2 = time_keyword2.index.tolist()
keyword2 = time_keyword2['Keyword'].tolist()
time2_keyword2_2020_21 = pd.DataFrame(
    {'Time': time2,
     '2020-2021': keyword2,
     })

ax = time1_keyword1_2018_19.plot(x='Time', y='2018-2019')
time2_keyword2_2020_21.plot(ax=ax, x='Time', y='2020-2021')

plt.title("Anxiety")
plt.xlabel('Months')
ax.set_xticklabels(['blank','April','June','August', 'November', 'January', 'March'])
plt.ylabel('Google Search Frequency')
plt.savefig(Constants.OUTPUT_LOC + 'anxiety_over_twotimeperiods..jpeg', bbox_inches='tight')