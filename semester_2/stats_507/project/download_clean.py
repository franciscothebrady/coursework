## download data and do some cleaning 

import os
import requests
import pandas as pd
import numpy as np
import helpers as h

## download and zip data file 
# cdc url
file_url = 'https://data.cdc.gov/api/views/hksd-2xuw/rows.csv?accessType=DOWNLOAD'
zip_path = 'cdc_data.zip'
# Download the file and zip it
h.download_and_zip(file_url, zip_path)

## read in data and describe
cdc_data = pd.read_csv(zip_path)
cdc_data.describe()
# print all column names
print(cdc_data.columns)

## print first 5 rows of Topic, Question, Response, and DataValue columns
print(cdc_data[['Topic', 'Question', 'Response', 'DataValue']].head())
## print all unique values of Question column
print(cdc_data['Question'].unique())

## reshape the data so that each question is a column and each row is a unique combination of Topic, Response, and DataValue




