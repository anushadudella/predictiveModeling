import time

import matplotlib.pyplot as plt
import numpy
from pytrends.request import TrendReq
from pathlib import Path
import pandas as pd


def getGoogleArray(keyword1, date1, date2, GEOPARAM):
    #GEOPARAM = 'US-NY'
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2], geo=GEOPARAM)
    df2 = pytrend.interest_over_time()
    filepath = Path('./' + keyword1 + 'Data.csv')
    df2.to_csv(filepath)

    return df2

def getDataFrame(keyword1, date1, date2, GEOPARAM):
    df3 = getGoogleArray(keyword1, date1, date2, GEOPARAM)
    #print(df3)
    dfkeyword = df3[keyword1].to_frame()

    return dfkeyword

#Corona Depression 0.64
#Corona Anxiety 0.4
#Covid 19 depression 0.53
#Covid 19 Anxiety 0.39
#Covid 19 Death 0.83
#Covid 19 Suicide -0.083
#Covid 19 Cough 0.411
#Covid 19 Blues -0.26
#Covid 19 Bipolar 0.26
#Covid 19 Anorexia 0.35
#Covid 19 Bulimia 0.058
#Covid 19 adhd -0.71


keyword1 = 'Covid 19'
keyword2_list = ['Autism', 'Death','Depression', 'Anxiety']
geoparam = ['US-FL','US-NY','US-NJ']

try:
    for geocode in geoparam:
        for keyword2 in keyword2_list:
            time_keyword1 = getDataFrame(keyword1,'2020-04-04', '2021-04-06', geocode)
            time_keyword2 = getDataFrame(keyword2,'2020-04-04', '2021-04-06', geocode)
            list1 = time_keyword1[keyword1].to_list()
            list2 = time_keyword2[keyword2].to_list()
            print(keyword1 + ',' + keyword2 + ',' + geocode + ',' + str(numpy.corrcoef(list1,list2).flat[1]))
            time.sleep(20)
except Exception as e:
    print(e.args)

