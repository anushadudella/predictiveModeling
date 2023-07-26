import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import pandas as pd

def getGoogleArray(keyword1, date1, date2, GEOPARAM):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2], geo=GEOPARAM)
    df2 = pytrend.interest_over_time()
    # filepath = Path('/Users/kkaa_austin/PycharmProjects/predictiveModeling/covidCasesKeywords' + keyword1 + 'Data.csv')
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

time_keyword1 = getDataFrame('depression','2018-04-04','2019-04-06', 'US-NY')
time_keyword2 = getDataFrame('depression','2020-04-05','2021-04-06', 'US-NY')

time1 = time_keyword1.index.tolist()
keyword1 = time_keyword1['Keyword'].tolist()
time1_keyword1_2018_19 = pd.DataFrame(
    {'Time': time1,
     'Depression 2018-2019 US-NY': keyword1,
    })

time2 = time_keyword2.index.tolist()
keyword2 = time_keyword2['Keyword'].tolist()
time2_keyword2_2020_21 = pd.DataFrame(
    {'Time': time2,
     'Depression 2020-2021 US-NY': keyword2,
    })

ax = time1_keyword1_2018_19.plot(x='Time', y='Depression 2018-2019 US-NY')
time2_keyword2_2020_21.plot(ax=ax, x='Time', y='Depression 2020-2021 US-NY')

plt.xlabel('Time in Weeks')
plt.ylabel('Freq. of Keywords')
plt.show()
