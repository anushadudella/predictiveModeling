import matplotlib
from pytrends.request import TrendReq
from pathlib import Path
import pandas as pd
import pandas as py
import matplotlib.pyplot as plt
from getGoogleData import getRSquared

def getGoogleArray(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2], geo='US')
    df2 = pytrend.interest_over_time()
    filepath = Path('/home/adudella/PycharmProjects/googleTrends/' + keyword1 + 'Data.csv')
    df2.to_csv(filepath)
    return df2

dfBulimia = getGoogleArray('Overweight', '2020-04-04', '2021-04-06')
dfCOVID = getGoogleArray('Corona', '2020-04-04', '2021-04-06')
dfBulimiaList = dfBulimia['Overweight'].tolist()
dfCOVIDList = dfCOVID['Corona'].tolist()

dfboth = pd.DataFrame(
    {'Overweight': dfBulimiaList,
     'Corona': dfCOVIDList,
    })

corr = getRSquared(dfboth,'Overweight', 'Corona')
print(corr)

plt.scatter(dfboth['Overweight'], dfboth['Corona'], label='scatterplot')
plt.legend(loc='best', fontsize=16)
plt.xlabel('Overweight')
plt.ylabel('Corona')
plt.show()