import numpy as np
import pandas as pd
from sklearn.externals import joblib

def RF():

# load model
    classifier = joblib.load("./train_model.m")

# load dataset
    dataset=pd.read_csv("./result.csv")

    x=dataset.iloc[1:2,:-1].values
    y=dataset.iloc[1:2,-1].values

    y_test = classifier.predict(x)
    if(y_test == 0):print('0',end='')
    else:print('1',end='')
