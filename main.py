import pandas as pd 
import numpy as np 
from datetime import datetime
import swifter

data = pd.read_csv('data.csv')

# City bike usage for pandemic period if the pandemic DID NOT happen -----------------------
#Drop irrelevant fields 
for col in data.columns: 
    print(col)
dropped = data.drop(columns=['STATION ID', 'LAST UPDATED', 'NAME', 'STATUS', 'ADDRESS'])
#Convert time to datetime objects for comparison 
print(dropped.to_string(max_rows=12))
timeObjs = dropped.swifter.apply(lambda a : a[1]*2, axis=1)
#timeObjs = dropped.apply(lambda x : datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), axis=1) 
print(timeObjs.to_string(max_rows=5))


