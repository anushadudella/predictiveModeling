import numpy as np
import pandas as pd
import os

def lag(x,y):
    if n == 0:
        return x
    if isinstance(x, pd.Series):
        return x.shift(n)
    else:
        x = pd.Series(x)
        return x.shiftn(y)

    x = x.copy()
    x[y:] = x[0:-y]
    x[:y] = np.nan
    return x

for dirname, _, filenames in os.walk('/kaggle.input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
