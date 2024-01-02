import pandas as pd 
import numpy as np 
from datetime import datetime

data = pd.read_csv('data.csv')

# City bike usage for pandemic period if the pandemic DID NOT happen -----------------------
#Drop irrelevant fields 
bp = data.copy(deep=True)
bp.drop(['STATION ID', 'LAST UPDATED', 'NAME', 'STATUS', 'ADDRESS'])
#Convert time to datetime objects for comparison 
bp['TIME OBJ'] = bp.apply(lambda row : datetime.strptime(row[0], '%y-%m-%d %H:%M:%S')) 



