#Used to concatenate and sort the csv files 
import pandas as pd

#Data files 
db_2018_q3 = pd.read_csv('dublinbikes_20180701_20181001.csv')
db_2018_q4 = pd.read_csv('dublinbikes_20181001_20190101.csv')
db_2019_q1 = pd.read_csv('dublinbikes_20190101_20190401.csv')
db_2019_q2 = pd.read_csv('dublinbikes_20190401_20190701.csv')
db_2019_q3 = pd.read_csv('dublinbikes_20190701_20191001.csv')
db_2019_q4 = pd.read_csv('dublinbikes_20191001_20200101.csv')

dbs = [db_2019_q2, db_2019_q3, db_2019_q4]

#Concatenating 
dataset = pd.concat(
    dbs,
    axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True,
)
#Sorting 
print("Sorting ...")
sorted = dataset.sort_values(by=['STATION ID'], kind='mergesort')
print("Sorted.\nOutputting to csv ..")
sorted.to_csv('data.csv', index=False)
print("Finished.")

