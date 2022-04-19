# -*- coding: utf-8 -*-

import pandas as pd
from infrastructure.mydict import MyDict


def gram():
    n = 3
    origin = pd.read_csv("./data.csv")
    mdict = MyDict()
    feature = origin["Feature"].str.split("|")
    for i, code in enumerate(feature):
        mdict.newLayer()
        if not type(code) == list:
            continue
        for method in code:
            length = len(method)
            if length < n:
                continue
            for start in range(length - (n - 1)):
                end = start + n
                mdict.mark(method[start:end])

    result = mdict.dict
    result['isMalware']=origin.isMalware
    pd.DataFrame(result, index=origin.index)\
                .to_csv("/home/group9/" + str(n) + "_gram.csv", index=False)
