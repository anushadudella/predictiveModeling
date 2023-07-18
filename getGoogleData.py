import pandas as pd
from pytrends.request import TrendReq
from numpy import mean
from sklearn.linear_model import LinearRegression
from numpy import std
from pathlib import Path

def getGoogleArray(keyword1, keyword2, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    print(df2)
    filepath = Path('/home/adudella/PycharmProjects/googleTrends/BulimiaData.csv')
    df2.to_csv(filepath)

    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword2], timeframe=[date1 + ' ' + date2])
    df3 = pytrend.interest_over_time()
    filepath = Path('/home/adudella/PycharmProjects/googleTrends/COVIDData.csv')
    df3.to_csv(filepath)

    x = df2.to_numpy()
    y = df3.to_numpy()
    return df2, df3

def getCustomTrends(keyword1, keyword2, date1, date2):
    Rs2 = customTrend(keyword1, keyword2, date1, date2)
    print(Rs2)

# def getHighestRSquared(r2):
#     z = r2.to_numpy()
#     maxValue = r2[0]
#     for x in z:
#         if r2[x] > maxValue
#             r2[x] = maxValue
#         else
#             continue
#         return maxValue

#r squared as parameter to function to help develop causality
