import pandas as pd
import numpy as np
import csv
import sys
from ethnicolr import census_ln, pred_census_ln

filepath = sys.argv[1]
file = pd.read_csv(filepath)

dataframe_stat = pred_census_ln(file, 'LAST NAME', 2010)
refreshed_dataframe= dataframe_stat[['FIRST NAME', 'LAST NAME', 'race']]
refreshed_dataframe.columns=['FIRST NAME','LAST NAME', 'ETHNICITY']
refreshed_dataframe.to_csv('Consumer_Data_10394_Sample2.csv', index =False)
