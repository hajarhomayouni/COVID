import sys
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
import csv



f=sys.argv[1]
x1=sys.argv[2]
x2=sys.argv[3]

dataFrame=pd.read_csv(f)
min_max=MinMaxScaler(feature_range=(0, 1))
dataFrame[[x1]]=min_max.fit_transform(dataFrame[[x1]])
dataFrame[[x2]]=min_max.fit_transform(dataFrame[[x2]])

result=mean_squared_error(dataFrame[[x1]],dataFrame[[x2]])
print(result)


