import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm,preprocessing,cross_validation
from sklearn.metrics import classification_report

style.use('fivethirtyeight')

# Not necessary, I just do this so I do not show my API key.
api_key = 'BB7funzM_vKkFhjizJyL'

def create_labels(cur_hpi,fut_hpi):
    if fut_hpi>cur_hpi:
        return 1
    else:
        return 0
def moving_average(values):
    ma = mean(values)
    return ma

housing_data = pd.read_pickle('HPI.pickle')
housing_data.rename(columns={'Value':'United States'}, inplace=True)
housing_data = housing_data.pct_change()


housing_data.replace([np.inf,-np.inf],np.nan,inplace=True)

housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)
housing_data.dropna(inplace=True)

housing_data['label'] = list(map(create_labels,housing_data['United States'], housing_data['US_HPI_future']))

# print(housing_data.tail())

X = np.array(housing_data.drop(['label','US_HPI_future'],1))
X = preprocessing.scale(X) #To change the data into -1 to 1
y = np.array(housing_data['label'])

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2)
#Train and test split
clf = svm.SVC(kernel='linear')
clf.fit(X_train,y_train)

print(clf.score(X_test,y_test))  

#Reporting
print(X_test,clf.predict(X_test))