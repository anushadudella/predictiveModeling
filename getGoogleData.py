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

    return df2, df3

def getRSquared(df, keyword1, keyword2):
    corr = df[keyword1].corr(df[keyword2])
    return corr

def getGoogleSpecificDataFrame1(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    # filepath = Path('/home/adudella/PycharmProjects/googleTrends/BulimiaData.csv')
    # df2.to_csv(filepath)

    x = df2.to_numpy()
    return df2
def getGoogleSpecificDataFrame2(keyword2, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword2], timeframe=[date1 + ' ' + date2])
    df3 = pytrend.interest_over_time()
    # filepath = Path('/home/adudella/PycharmProjects/googleTrends/COVIDData.csv')
    # df3.to_csv(filepath)

    y = df3.to_numpy()
    return df3

z = getGoogleSpecificDataFrame1('bulimia', '2020-04-04', '2021-04-06')
print(z)

