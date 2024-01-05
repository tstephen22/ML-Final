#Used to concatenate and sort the csv files 
import pandas as pd
import glob
# print("Reading training ...")
# #Data files 
# db_2018_q3 = pd.read_csv('dublinbikes_20180701_20181001.csv')
# db_2018_q4 = pd.read_csv('dublinbikes_20181001_20190101.csv')
# db_2019_q1 = pd.read_csv('dublinbikes_20190101_20190401.csv')
# db_2019_q2 = pd.read_csv('dublinbikes_20190401_20190701.csv')
# db_2019_q3 = pd.read_csv('dublinbikes_20190701_20191001.csv')
# db_2019_q4 = pd.read_csv('dublinbikes_20191001_20200101.csv')

# dbs = [db_2018_q3, db_2018_q4, db_2019_q1, db_2019_q2, db_2019_q3, db_2019_q4]

# #Concatenating 
# dataset = pd.concat(
#     dbs,
#     axis=0,
#     join="outer",
#     ignore_index=False,
#     keys=None,
#     levels=None,
#     names=None,
#     verify_integrity=False,
#     copy=True,
# )
# print(">> Finished.")
# #Sorting 
# print("Sorting by station ...")
# sorted = dataset.sort_values(by=['STATION ID'], kind='mergesort')
# print(">> Sorted.\nOutputting to csv ..")
# sorted.to_csv('data.csv', index=False)
# print(">> Finished.")

# print("Reading pandemic period (20-3-2020) - (22-1-2022)")
# #Pandemic files 
# pd_2020_q1 = pd.read_csv('pandemic_period/pandemic_20200320_20200401.csv')
# pd_2020_q2 = pd.read_csv('pandemic_period/pandemic_20200401_20200701.csv')
# pd_2020_q3 = pd.read_csv('pandemic_period/pandemic_20200701_20201001.csv')
# pd_2020_q4 = pd.read_csv('pandemic_period/pandemic_20201001_20210101.csv')
# pd_2021_q1 = pd.read_csv('pandemic_period/pandemic_20210101_20210401.csv')
# pd_2021_q2 = pd.read_csv('pandemic_period/pandemic_20210401_20210701.csv')
# pd_2021_q3 = pd.read_csv('pandemic_period/pandemic_20210701_20211001.csv')
# pd_2021_q4 = pd.read_csv('pandemic_period/pandemic_20211001_20220101.csv')

# pandemic_2020_data = [pd_2020_q1, pd_2020_q2, pd_2020_q3, pd_2020_q4]
# pandemic_2021_data = [pd_2021_q1, pd_2021_q2, pd_2021_q3, pd_2021_q4]

# print(">> Done.")
# print("Creating csv's ...")
# pandemic_2020_csv = pd.concat(
#     pandemic_2020_data,
#     axis=0,
#     join="outer",
#     ignore_index=False,
#     keys=None,
#     levels=None,
#     names=None,
#     verify_integrity=False,
#     copy=True,
# )
# pandemic_2021_csv = pd.concat(
#     pandemic_2021_data,
#     axis=0,
#     join="outer",
#     ignore_index=False,
#     keys=None,
#     levels=None,
#     names=None,
#     verify_integrity=False,
#     copy=True,
# )
# print(">> Outputting csv's ..")
# pandemic_2020_csv.to_csv('pandemic_2020.csv', index=False)
# print(">> Outputted Pandemic 2020 csv file.")
# pandemic_2021_csv.to_csv('pandemic_2021.csv', index=False)
# print(">> Outputted Pandemic 2021 csv file.")
# print("Finished.")

print("Reading post pandemic period (1-2-2022 - 31-12-2023)")
# This is done manually as order needs to be presevered 
pp_2022_02 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-02.csv')
pp_2022_03 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-03.csv')
pp_2022_04 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-04.csv')
pp_2022_05 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-05.csv')
pp_2022_06 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-06.csv')
pp_2022_07 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-07.csv')
pp_2022_08 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-08.csv')
pp_2022_09 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-09.csv')
pp_2022_10 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-10.csv')
pp_2022_11 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-11.csv')
pp_2022_12 = pd.read_csv('post_pandemic/dublinbike-historical-data-2022-12.csv')

pp_2023_01 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-01.csv')
pp_2023_02 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-02.csv')
pp_2023_03 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-03.csv')
pp_2023_04 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-04.csv')
pp_2023_05 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-05.csv')
pp_2023_06 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-06.csv')
pp_2023_07 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-07.csv')
pp_2023_08 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-08.csv')
pp_2023_09 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-09.csv')
pp_2023_10 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-10.csv')
pp_2023_11 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-11.csv')
pp_2023_12 = pd.read_csv('post_pandemic/dublinbike-historical-data-2023-12.csv')

post_pandemic_list = [pp_2022_02,pp_2022_03, pp_2022_04,pp_2022_05,pp_2022_06,pp_2022_07,pp_2022_08,pp_2022_09,pp_2022_10,pp_2022_11,pp_2022_12,
                      pp_2023_01, pp_2023_02, pp_2023_03,pp_2023_04,pp_2023_05,pp_2023_06,pp_2023_07,pp_2023_08,pp_2023_09,pp_2023_10,pp_2023_11,pp_2023_12]
print(">> Done.")
print("Creating csv's ...")
post_pandemic_csv = pd.concat(
     post_pandemic_list,
     axis=0,
     join="outer",
     ignore_index=False,
     keys=None,
     levels=None,
     names=None,
     verify_integrity=False,
     copy=True,
 )
print(">> Outputting csv ..")
post_pandemic_csv.to_csv('post_pandemic_data.csv', index=False)
print(">> Outputted post pandemic csv file.")
print("Finished.")