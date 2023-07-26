import matplotlib.pyplot as plt
import pandas as pd
from pytrends.request import TrendReq
from numpy import mean
from sklearn.linear_model import LinearRegression
from numpy import std
from getGoogleData import getGoogleArray

pytrend = TrendReq()
pytrend.build_payload(kw_list=['bulmia'], timeframe=['2020-04-04 2021-04-10'])
df2 = pytrend.interest_over_time()

pytrend = TrendReq()
pytrend.build_payload(kw_list=['Anxiety'], timeframe=['2020-04-04 2021-04-10'])
df3 = pytrend.interest_over_time()

x, y = getGoogleArray('bulmia', 'Anxiety', '2020-04-04', '2021-04-10')

plt.scatter(x, y, c="purple")

# To show the plot
plt.xlabel("COVID")
plt.ylabel("Anxiety")
plt.show()