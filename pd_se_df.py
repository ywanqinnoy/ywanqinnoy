import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])
print(obj)
obj = pd.Series([4.5, 7.8, -5.3, 3.6], index=['d','b','c','a'])
print(obj)

obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)