from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

df = pd.read('/home/adudella/PycharmProjects/googleTrends/BulimiaData.csv')
df['date'] = pd.to_datetime(df['date'],infer_datetime_format=True)
df = df.set_index(['Month'])
df.head(3)
plt.figure(figsize=(15,7))
plt.title("Number of Bulimia Search Frequencies by Date")
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.plot(df)
plt.show()
