import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd
from getGoogleData import getGoogleArray
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

# def getDataFrame():
df4, df5 = getGoogleArray('bulimia', 'covid', '2020-04-04', '2021-04-10')
dftimes1 = df4.index.tolist()
dfkeyword1 = df4['bulimia'].tolist()
time_keyword1 = pd.DataFrame(
    {'Time': dftimes1,
     'Bulimia': dfkeyword1,
    })
# return time_keyword1

# sns.lineplot(time_keyword)
# print(time_keyword)
# # plt.show()

# def getDataFrame2():
dftimes2 = df5.index.tolist()
dfkeyword2 = df5['covid'].tolist()
time_keyword2 = pd.DataFrame(
    {'Time': dftimes2,
     'Covid': dfkeyword2,
    })
#sns.lineplot(time_keyword)
#plt.show()
# return time_keyword2

ax = time_keyword1.plot(x='Time', y='Bulimia')
time_keyword2.plot(ax=ax, x='Time', y='Covid')
#
plt.show()

# #Stationarity
# rolling_mean = df4.rolling(7).mean()
# rolling_std = df4.rolling(7).std()
# plt.plot(df4, color="blue",label="Original Bulmia Data")
# plt.plot(rolling_mean, color="red", label="Rolling Bulmia Mean")
# plt.plot(rolling_std, color="black", label="Rolling Bulmia Standard Deviation")
# # plt.show()

# #Predictive forecasting
# df4['Date'] = df4.index
# train = df4[df4['Date'] < pd.to_datetime("2024-08", format='%Y-%m')]
# train['train'] = train['Bulmia']
# del train['Date']
# del train['Bulmia']
# test = df4[df4['Date']] >= pd.to_datetime("2024-08", format='%Y-%m')
# del test['Date']
# test['test'] = test['Bulmia']
# del test['Bulmia']
# plt.plot(train, color = "black")
# plt.plot(test, color = "red")
# plt.title("Train/Test split for Bulmia Data")
# plt.show()

# # #Dickey fuller test
# # adft = adfuller(df4,autolag="AIC")
# # output_df = pd.DataFrame({"Values":[adft[0],adft[1],adft[2],adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']]  , "Metric":["Test Statistics","p-value","No. of lags used","Number of observations used",
# # "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
# # print(output_df)
#
# autocorrelation_lag3 = df4['#Passengers'].autocorr(lag=3)
# print("Three Month Lag: ", autocorrelation_lag3)
#
# autocorrelation_lag6 = df4['#Passengers'].autocorr(lag=6)
# print("Six Month Lag: ", autocorrelation_lag6)

# autocorrelation_lag9 = df['#Passengers'].autocorr(lag=9)
# print("Nine Month Lag: ", autocorrelation_lag9)
#
# #decompose
# decompose = seasonal_decompose(df4['#Passengers'],model=additive, period=7)
# decompose.plot()
# plt.show()

# #autocorrelation
# df['Date'] = df.index
# train = df[df['Date'] < pd.to_datetime("1960-08", format='%Y-%m')]
# train['train'] = train['#Passengers']
# del train['Date']
# del train['#Passengers']
# test = df[df['Date'] >= pd.to_datetime("1960-08", format='%Y-%m')]
# del test['Date']
# test['test'] = test['#Passengers']
# del test['#Passengers']
# plt.plot(train, color = "black")
# plt.plot(test, color = "red")
# plt.title("Train/Test split for Passenger Data")
# plt.ylabel("Passenger Number")
# plt.xlabel('Year-Month')
# sns.set()
# plt.show()

#
# def gcorr(df3, df4):
# x = df3.to_numpy()
# y = df4.to_numpy()
#
# for z in x:
#     maxValue1 = x[0]
#     if x[z] > maxValue1
#         maxValue1 = x[z]
# for q in y:
#     maxValue2 = df4[0]
#     if y[q] > maxValue2
#         maxValue2 = df4[q]
