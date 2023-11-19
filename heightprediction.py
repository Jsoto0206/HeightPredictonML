# -*- coding: utf-8 -*-
"""heightprediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bKLJUGLSzhVJBNHVHCLCjhraHrwXcQZs
"""

import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/Jsoto0206/Dataholding/main/person_datatest2.csv')
df = pd.read_csv('https://raw.githubusercontent.com/Jsoto0206/Dataholding/main/person_datatest4.csv')
df.head(183) #this prints out the current data for google colab

X = df[['Weight', 'Sex', 'Age', 'Continent']]
y = df['Height Class']

X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})
X['Continent'] = X['Continent'].map({'Africa': 0, 'Antarctica': 1, 'Asia': 2, 'Australia': 3, 'Europe': 4, 'North America': 5, 'South America': 6})#antartica is a bit redundent but was used for tests

"""this causes a scary error lol

<ipython-input-7-63e963a25d28>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})
<ipython-input-7-63e963a25d28>:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  X['Continent'] = X['Continent'].map({'Africa': 0, 'Antarctica': 1, 'Asia': 2, 'Australia': 3, 'Europe': 4, 'North America': 5, 'South America': 6})

which is fine since we are tyring to slice the data frame 
"""

import matplotlib.pyplot as plt #this is used for data visualaizaton for colab
a = df['Continent']
b = df['Age']
plt.scatter(a, y)
plt.show()

from sklearn.model_selection import train_test_split #divides the data for testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=50, random_state=42)

from sklearn.neighbors import KNeighborsClassifier
num = 5
knn = KNeighborsClassifier(n_neighbors=num) #this is where the magic happens
knn.fit(X_train, y_train)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))