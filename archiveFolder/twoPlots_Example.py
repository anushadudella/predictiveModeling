import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

df1 = pd.DataFrame(
   dict(
      name=['John', 'James', 'Stephen', 'Kandy'],
      age=[23, 45, 12, 34]
   )
)
print(df1)

df2 = pd.DataFrame(
   dict(
      subject=['Math', 'Physics', 'Chemistry', 'Biology'],
      marks=[67, 98, 90, 75]
   )
)

ax = df1.plot(x='name', y='age')
df2.plot(ax=ax, x='subject', y='marks')

plt.show()