import sys
import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from pytrends.request import TrendReq
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from pathlib import Path

import Constants


def insert(df, row):
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc + 1] = row

# GOOGLE TRENDS API PART

def getGoogleArray(keyword1, date1, date2):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword1], timeframe=[date1 + ' ' + date2])
    df2 = pytrend.interest_over_time()
    return df2


def getDataFrame(keyword1, date1, date2):
    df3 = getGoogleArray(keyword1, date1, date2)
    return df3

def getScaledData(dfUSCovid):

    uscasesbydate = pd.DataFrame(columns=['date', 'casesbydate'])
    uscasesbyweek = pd.DataFrame(columns=['weekdate', 'casesbyweek'])

    prevdate = Constants.COVID_START_DATE
    cases_sum = 0

    for index, row in dfUSCovid.iterrows():
        if (row['date'] == prevdate):
            cases_sum = cases_sum + row['cases']
        else:
            rowdata = []
            rowdata.append(prevdate)
            rowdata.append(str(cases_sum))
            insert(uscasesbydate, rowdata)
            cases_sum = 0
            prevdate = row['date']

    prevdate = Constants.COVID_START_DATE
    cases_sum = 0

    for index, row in uscasesbydate.iterrows():
        if (index % 7 != 0):
            cases_sum = cases_sum + int(row['casesbydate'])
        else:
            rowdata = []
            rowdata.append(row['date'])
            rowdata.append(cases_sum)
            insert(uscasesbyweek, rowdata)
            cases_sum = 0

    df_max_scaled = uscasesbyweek.copy()

    # apply normalization techniques (scales it down to value between 0 and 1)
    df_max_scaled['casesbyweek'] = (df_max_scaled['casesbyweek'] - df_max_scaled['casesbyweek'].min()) / (
            df_max_scaled['casesbyweek'].max() - df_max_scaled['casesbyweek'].min())

    df_max_scaled['casesbyweek'] = round(df_max_scaled['casesbyweek'] * 100)

    return df_max_scaled


def main():

    # observations / data
    directory = Constants.INPUT_LOC
    files = list(Path(directory).glob('*'))

    df = pd.DataFrame()
    lsDataframes = []

    try:
        if (len(files) < 1):
            raise Exception()
        else:
            for file in files:
                df_temp = pd.read_csv(file)
                lsDataframes.append(df_temp)
            df = pd.concat(lsDataframes)
            print(df.size)
    except:
        print(" No COVID case files found ")
        sys.exit()

    date_df = pd.DataFrame(df[(df['date'] >= Constants.COVID_START_DATE) & (df['date'] <= Constants.COVID_END_WEEK)])
    US_df = pd.DataFrame(date_df, columns=['date', 'cases'])

    US_df.sort_values(by=['date'])


# Get a scaled dataframe to be uniform with google trands data

    df_max_scaled = getScaledData(US_df)

    all_keyworddata = getDataFrame('ADHD', Constants.COVID_START_DATE, Constants.COVID_END_WEEK)
    time_keyword1 = all_keyworddata

    time_keyword1 = time_keyword1.drop(['isPartial'], axis=1)
    google_trends = time_keyword1['ADHD'].to_list()

    usCovidData = df_max_scaled['casesbyweek']
    usCovidData = usCovidData.astype(int)
    lstUSCoviddata = usCovidData.to_list()

    # estimating coefficients

    x = np.array(lstUSCoviddata)
    y = np.array(google_trends)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = Constants.TEST_SZ)

    model = LinearRegression()
    model.fit(x_train.reshape(-1, 1), y_train)

    # write out put values to a file

    fOutput = open(Constants.LINEAR_REG_OUTPUT, "w")

    fOutput.write(' Linear regression Model Coefficient : ' + str(model.coef_) + Constants.NEW_LINE)

    #predicting the test values
    predictions = model.predict(x_test.reshape(-1,1))

    plt.scatter(y_test, predictions)
    plt.show()
    plt.savefig(Constants.OUTPUT_LOC + 'scatterplot.jpeg', bbox_inches='tight')

    plt.hist(y_test - predictions)
    plt.show()
    plt.savefig(Constants.OUTPUT_LOC + 'residualsplot.jpeg', bbox_inches='tight')

    fOutput.write(' Mean Absolute Error ' + str(metrics.mean_absolute_error(y_test, predictions)) + Constants.NEW_LINE)
    fOutput.write(' Mean Squared Error ' + str(metrics.mean_squared_error(y_test, predictions)) + Constants.NEW_LINE)
    fOutput.write(' Root Mean Squared Error ' + str(np.sqrt(metrics.mean_squared_error(y_test, predictions))) + Constants.NEW_LINE)

    fOutput.close()

if __name__ == "__main__":
    main()