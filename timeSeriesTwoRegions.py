import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from pathlib import Path
import pandas as pd

def getGoogleArray(keyword1, date1, date2, GEOPARAM):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2], geo=GEOPARAM)
    df2 = pytrend.interest_over_time()
    # filepath = Path(DATAPATH + keyword1 + '_' + date1 + '_' + date2 + '_' + 'Data.csv')
    # df2.to_csv(filepath)
    return df2

def getDataFrame(keyword1, date1, date2, GEOPARAM):
    df3 = getGoogleArray(keyword1, date1, date2, GEOPARAM)
    dftimes1 = df3.index.tolist()
    dfkeyword1 = df3[keyword1].tolist()
    time_keyword1 = pd.DataFrame(
    {'Time': dftimes1,
     'Anorexia': dfkeyword1,
    })
    return time_keyword1


    # print(dfkeyword)
    return dfkeyword

# def getGoogleArrayFourYears(keyword1, date1, date2, date3, date4, GEOPARAM):
#     pytrend = TrendReq()
#     pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2 + ' ' + date3 + ' ' + date4], geo=GEOPARAM)
#     df2 = pytrend.interest_over_time()
#     # filepath = Path(DATAPATH + keyword1 + '_' + date1 + '_' + date2 + '_' + 'Data.csv')
#     # df2.to_csv(filepath)
#     return df2
#
# def getDataFrameFourYears(keyword1, date1, date2, date3, date4, GEOPARAM):
#     df3 = getGoogleArrayFourYears(keyword1, date1, date2, date3, date4, GEOPARAM)
#     dftimes1 = df3.index.tolist()
#     dfkeyword1 = df3[keyword1].tolist()
#     time_keyword1 = pd.DataFrame(
#     {'Time': dftimes1,
#      'Depression': dfkeyword1,
#     })
#     return time_keyword1


keyword2 = 'Anorexia'
geoparam1 = 'US-TX'
geoparam2 = 'US-TX'

date1 = '2018-04-04'
date2 = '2019-04-06'
date3 = '2020-04-04'
date4 = '2021-04-06'

# DATAPATH = '/home/adudella/PycharmProjects/predictiveModeling/oneCountryHypothesis/' + keyword2 + '/'

try:
    #prints out for region1 across time
    time_keyword1 = getDataFrame(keyword2, date1, date4, geoparam1)
    print(time_keyword1)

    #prints out for region 2 across time
    time_keyword2 = getDataFrame(keyword2, date1, date4, geoparam2)
    print(time_keyword2)

    ax = time_keyword1.plot(x='Time', y='Anorexia')
    time_keyword2.plot(ax=ax, x='Time', y='Anorexia')
    plt.show()

except Exception as e:
    print(e.args)