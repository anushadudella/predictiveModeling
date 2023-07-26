import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from pathlib import Path
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

def getGoogleArray(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    filepath = Path('/home/adudella/PycharmProjects/googleTrends/' + keyword1 + 'Data.csv')
    df2.to_csv(filepath)
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

# sns.lineplot(time_keyword)
# print(time_keyword)
# # plt.show()

time_keyword1 = getDataFrame('Anorexia','2020-04-04', '2021-04-06')
time_keyword2 = getDataFrame('Anorexia','2021-04-04', '2022-04-06')
ax = time_keyword1.plot(x='Time', y='Keyword')
time_keyword2.plot(ax=ax, x='Time', y='Keyword')
#
plt.show()