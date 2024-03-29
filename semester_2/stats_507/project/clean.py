## read in data for dashboard 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# read in data
here = os.path.dirname(os.path.realpath(__name__))
cdc_data = pd.read_csv(os.path.join(here, 'U.S._Chronic_Disease_Indicators.csv'))

# create a list of the unique states
states = cdc_data['LocationDesc'].unique()
# create a list of the unique indicators
indicators = cdc_data['Question'].unique()
# create a list of the unique years
years = cdc_data['YearStart'].unique()