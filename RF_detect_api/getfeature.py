import pandas as pd
import numpy as np

def get():
    data = pd.read_csv("./3_gram.csv")
    listlabel = list(data.columns.values)
    labels = np.array(listlabel)

    data = pd.read_csv("./model.csv")
    listheader = list(data.columns.values)
    headers = np.array(listheader)

    result = []
    for i in range(0,headers.shape[0]-2):
        if(headers[i] in labels): result.append(1)
        else: result.append(0)
    result.append(2)
    result = np.array(result)

    data = pd.DataFrame(result)
    data.to_csv('./result1.csv')
    dataset=pd.read_csv("./result1.csv")
    data = dataset.values
    data = list(map(list,zip(*data)))
    data = pd.DataFrame(data)
    data.to_csv('./result.csv')
