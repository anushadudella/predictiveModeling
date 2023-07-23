import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd
from getGoogleData import getGoogleArray
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report

# Main file having the plotting of bulimia and covid

df4, df5 = getGoogleArray('bulimia', 'covid', '2020-04-04', '2021-04-10')
dftimes = df4.index.tolist()
dfkeyword1 = df4['bulimia'].tolist()
time_keyword1 = pd.DataFrame(
    {'Time': dftimes,
     'Bulimia': dfkeyword1,
    })

df4, df5 = getGoogleArray('bulimia', 'covid', '2020-04-04', '2021-04-10')
dftimes = df5.index.tolist()
dfkeyword2 = df5['covid'].tolist()
time_keyword2 = pd.DataFrame(
    {'Time': dftimes,
     'Covid': dfkeyword2,
    })

predict_dataframe = pd.DataFrame(
{'Bulimia': time_keyword1['Bulimia'].tolist(),
'Covid': time_keyword2['Covid'].tolist()
})

# print(predict_dataframe)
X= predict_dataframe[['Bulimia']]  #the top 3 features
Y= predict_dataframe[['Covid']]  #the target output

# print(X)
# print(Y)

X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=100)
# print(X_train)https://github.com/anushadudella/icr2023-predictiveModeling
# print(y_train)

logreg= LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
# print (X_test) #test dataset
# print (y_pred) #predicted values

print("Accuracy: ",metrics.accuracy_score(y_test, y_pred))