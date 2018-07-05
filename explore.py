import json
import pandas as pd
import numpy as np
from sklearn import tree

with open('train.json', 'r') as f:
    datastore = json.load(f)

df = pd.DataFrame(datastore)

feature_cols = ['ingredients']

#target_cols =['cuisine']

X = df.loc[:, feature_cols]

Y = df['cuisine']

print X.shape, Y.shape

print type(X), type(Y)


YArray= Y.as_matrix(columns=None)
print type(YArray)

XArray= X.as_matrix(columns=None)
print type(XArray)

print XArray.shape, YArray.shape

print XArray[0]
#X = np.empty(shape=(X.size,), dtype="S36")
dt_clf = tree.DecisionTreeClassifier()

dt_clf = dt_clf.fit(XArray,YArray)

#dt_prediction = dt_clf.predict(["baking powder", "eggs", "all-purpose flour", "raisins", "milk", "white sugar"])
