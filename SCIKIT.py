# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:37:45 2021
SCIKIT
@author: bunya
"""
import os 
os.getcwd()
os.chdir("C:\\Users\\bunya\\python")
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
type(iris)
iris.keys()
iris.data
iris.target
iris.target_names
iris.data.shape
iris.DESCR
from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.3)
x_train.data.shape
x_test.data.shape
y_train.data.shape
y_test.data.shape


#  Preprocessing
from sklearn import preprocessing
# iris_scaled = pd.DataFrame(preprocessing.scale(iris_data))
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
# we create the model using the training objects
lr.fit(x_train, y_train)
# we view the coefficients
print(lr.intercept_)
lr.coef_
# we predict the membership for the test objects
pred = lr.predict(x_test)
 print(pred)

from sklearn import metrics
print('MAE', metrics.mean_absolute_error(y_test, pred))
print('MSE', metrics.mean_squared_error(y_test, pred))
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, pred))
metrics.explained_variance_score(y_test, pred)


#  we cannot use the k-neighbor algorithm on the iris dataset,
#we limit >>> from sklearn.neighbors import KNeighborsClassifier
>>> knn = KNeighborsClassifier(n_neighbors = 3)
>>>   x_train = from the dataset we will use the variables except the label
>>> y_train = the test labels
>>> x_test = new data
>>> y_test = new data labels
>>> knn.fit(x_train, y_train)
>>> new_pred = knn.predict(x_new)
>>> print(new_pred)
>>> from sklearn.metrics import classification_report, 
confusion_matrix
>>> print(confusion_matrix(y_test, y_pred))
>>> print(classification_report(y_test, y_pred))

"""  Cross-validation consists of dividing a dataset into a number of equal parts 
generally indicated by k (often five or ten parts) then testing the adequacy 
of the prediction model on these k groups."""

>>> from sklearn.model_selection import cross_val_score
>>> cv5 = cross_val_score(model, x_train, y_train, cv = 5)
>>> cv10 = cross_val_score(model, x_train, y_train, cv = 10)
>>> print(np.mean(cv5))
>>> print(np.mean(cv10))


  """"Support Vector Machine
Support Vector Machine (SVM) is used to determine the boundary 
between items belonging to two different classes, then projecting them 
into multidimensional space to discern the hyperplane that maximizes 
margins between the two sets of data."""

>>> from sklearn.svm import SVC
>>> clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
>>> clf.score(x_test, y_test)
>>> from sklearn.model_selection import cross_val_predict
>>> pred = cross_val_predict(clf, iris.data, iris.target, cv=10)
>>> metrics.accuracy_score(iris.target, pred)

 """" Decision Trees
The basic idea behind a decision tree is a divide et impera model, in which 
at each step we can reduce variability between nodes. Let’s us start with 
the entire dataset, which is then divided into smaller groups that are based 
more homogeneously and intrinsically on internal characteristics.
""""
>>> from sklearn.tree import DecisionTreeClassifier
>>> dtc = DecisionTreeClassifier()
>>> dtc = dtc.fit(x_train, y_train)
>>> pred = dtc.predict(y_test)
>>> sklearn.metrics.confusion_matrix(y_test, pred)
>>> sklearn.metrics.accuracy_score(y_test, pred)
>>> sklearn.metrics.classification_report(y_test, pred)

>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4)
>>> kmeans.fit(df)
>>> pred = kmeans.predict(df)
>>> pred

 """" Managing Dates
Managing dates using Python is important, especially when dealing w
time series representations. We can handle dates using the datetime 
package and pandas. First, we must import datetime.""""
>>> import datetime as dt
# we create a first object that contains 
>>> t1 = dt.time(19, 43 , 30)
>>> print(t1)


# we can query the created object about the year, the month, 
the day
>>> today = dt.date.today()
>>> today.year
>>> today.month
 t2 = dt.date(2016, 5, 20)
Let’s carry on with date management using pandas.
>>> import pandas as pd
# we can manage various data formats through Timestamp
>>> pd.Timestamp("2016-3-7")
>>> pd.Timestamp("2016/4/10")
>>> pd.Timestamp("2015, 12, 10")
>>> pd.Timestamp("2015, 12, 10 12:42:57")
>>>   date1 = ["2016/4/10", "2015, 12, 10", "2015, 12, 10 
12:42:57"] 




























