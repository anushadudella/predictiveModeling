import pandas as pd

time_stamps = pd.series(pd.date_range(start='04/06/2020', end = '04/11/2021')
time = df4.index.toList()
frequency = df4['covid'].toList()

ts_plot = performance.plot(kind='line',\title = 'Graph')
ts.plot.grid()

ts.plot_legend(loc='upper right')