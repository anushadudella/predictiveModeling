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

def getGoogleArray(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    # filepath = Path('/Users/kkaa_austin/PycharmProjects/PredictCovid/' + keyword1
    #                 + '_' + date1 + '_' + date2 + '_' + 'Data.csv')
    # df2.to_csv(filepath)
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


time_keyword1 = getDataFrame('insomnia', '2018-04-08', '2019-04-06')
time_keyword2 = getDataFrame('insomnia', '2020-04-05', '2021-04-03')

time1 = time_keyword1.index.tolist()
time1_series = time_keyword1.index
keyword1 = time_keyword1['Keyword'].tolist()
keyword1_series = time_keyword1['Keyword']

time1_keyword1_2018_19 = pd.DataFrame(
    {'Time': time1,
     'Insomnia 2018-2019': keyword1,
     })

time2 = time_keyword2.index.tolist()
keyword2 = time_keyword2['Keyword'].tolist()
keyword2_series = time_keyword2['Keyword']

time2_keyword2_2020_21 = pd.DataFrame(
    {'Time': time2,
     'Insomnia 2020-2021': keyword2,
     })

ax = time1_keyword1_2018_19.plot(x='Time', y='Insomnia 2018-2019')
time2_keyword2_2020_21.plot(ax=ax, x='Time', y='Insomnia 2020-2021')

plt.xlabel('Time in Weeks')
plt.ylabel('Freq. of Keywords')

# first create a dataframe with 2 columns of data from the
# 2 timeframes we have above time1_keyword1_2020_21 and time1_keyword1_2018_19
# Now the data frame will look like 2018_19_Depression and 2020_21_Depression by week

my_df_dict2 = {'2018_19' : keyword1_series , '2020_21' : keyword2_series}
my_df = pd.DataFrame(my_df_dict2)

fOutput = open(Constants.ONE_REGION_OUTPUT, "w")

euc_dist = euclidean_distances(my_df.T)
fOutput.write(str(euc_dist))
fOutput.close()