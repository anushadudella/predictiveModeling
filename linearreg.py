import pandas as pd
import plotly.express as px
import pmdarima as pm
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from pytrends.request import TrendReq
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


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
    dftimes1 = df3.index.tolist()
    dfkeyword1 = df3[keyword1].tolist()
    time_keyword1 = pd.DataFrame(
        {'Time': dftimes1,
         'ADHD': dfkeyword1,
         })
    return df3




def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():

    # observations / data
    df2020 = pd.read_csv('/home/adudella/PycharmProjects/predictiveModeling/covidCasesKeywords/us-counties-2020.csv')
    df2021 = pd.read_csv('/home/adudella/PycharmProjects/predictiveModeling/covidCasesKeywords/us-counties-2021.csv')

    combine_df = [df2020, df2021]
    df = pd.concat(combine_df)

    date_df = pd.DataFrame(df[(df['date'] >= '2020-04-05') & (df['date'] <= '2021-12-31')])
    my_us_df = pd.DataFrame(date_df, columns=['date', 'cases'])

    my_us_df.sort_values(by=['date'])
    cases_sum = 0
    prevdate = '2020-04-05'

    uscasesbydate = pd.DataFrame(columns=['date', 'casesbydate'])
    uscasesbyweek = pd.DataFrame(columns=['weekdate', 'casesbyweek'])

    rowdata = []
    for index, row in my_us_df.iterrows():
        if (row['date'] == prevdate):
            cases_sum = cases_sum + row['cases']
        else:
            rowdata = []
            rowdata.append(prevdate)
            rowdata.append(str(cases_sum))
            insert(uscasesbydate, rowdata)
            cases_sum = 0
            prevdate = row['date']

    prevdate = '2020-04-05'
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

    # apply normalization techniques (scales it down)
    df_max_scaled['casesbyweek'] = (df_max_scaled['casesbyweek'] - df_max_scaled['casesbyweek'].min()) / (
            df_max_scaled['casesbyweek'].max() - df_max_scaled['casesbyweek'].min())

    df_max_scaled['casesbyweek'] = round(df_max_scaled['casesbyweek'] * 100)

    all_keyworddata = getDataFrame('ADHD', '2020-04-05', '2021-12-26')
    time_keyword1 = all_keyworddata

    time_keyword1 = time_keyword1.drop(['isPartial'], axis=1)
    google_trends = time_keyword1['ADHD'].to_list()

    usCovidData = df_max_scaled['casesbyweek']
    usCovidData = usCovidData.astype(int)
    lstUSCoviddata = usCovidData.to_list()

    # estimating coefficients

    x = np.array(lstUSCoviddata)
    y = np.array(google_trends)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

    model = LinearRegression()
    model.fit(x_train.reshape(-1, 1), y_train)

    print(model.coef_)

    #predicting the test values
    predictions = model.predict(x_test.reshape(-1,1))

    plt.scatter(y_test, predictions)

    plt.xlabel('US COVID-19 cases')
    plt.ylabel('ADHD Search Frequency')
    plt.title('Linear Regression')
    plt.show()
    plt.hist(y_test - predictions)
    plt.title('Residual Error Plot')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.show()

    print(metrics.mean_absolute_error(y_test, predictions))
    print(metrics.mean_squared_error(y_test, predictions))
    print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))


if __name__ == "__main__":
    main()