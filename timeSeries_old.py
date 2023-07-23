import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd
from getGoogleData import getGoogleArray
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

#OLD ONE FOR FUNCTIONALITY PURPOSES (WORKS)
# def getDataFrame():
df4, df5 = getGoogleArray('insomina', 'covid', '2020-04-04', '2021-04-10')
dftimes1 = df4.index.tolist()
dfkeyword1 = df4['insomnia'].tolist()
time_keyword1 = pd.DataFrame(
    {'Time': dftimes1,
     'Insomnia': dfkeyword1,
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

ax = time_keyword1.plot(x='Time', y='Insomnia')
time_keyword2.plot(ax=ax, x='Time', y='Covid')
#
plt.show()
