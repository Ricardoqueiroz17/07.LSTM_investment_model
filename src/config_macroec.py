# Compilations of libraries

# API INSTALL
#In case you need to install Nasdaq or FRED API source
#pip install nasdaq-data-link
#!pip install fredapi

#===========MY OWN LIBRARIES AND CLASSES -.py files in the same folder=======================================

from src.Databases import dataset
from src.increase_dataset import increase_dataset
from src.FutureReturn_calc import stopLossFutRet
from src.PerfBacktest import perf_backtest

#====================================================================================

#Data source FRED St Louis
from fredapi import Fred
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import copy #enables deep copies of dictionaries and other data

#From Sklearn
from sklearn.preprocessing import MinMaxScaler

# visualization - plotting & outputs
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.font_manager
plt.style.use('seaborn')
import cufflinks as cf
cf.set_config_file(offline=True)
import seaborn as sns