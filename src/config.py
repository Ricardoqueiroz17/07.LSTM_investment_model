# Compilations of libraries

#===========MY OWN LIBRARIES AND CLASSES -.py files in the same folder=======================================
from src.Databases import dataset
from src.increase_dataset import increase_dataset
from src.FutureReturn_calc import stopLossFutRet
from src.PerfBacktest import perf_backtest
#====================================================================================

#Yfinance
import yfinance as yf
from yahoofinancials import YahooFinancials

# basic imports
import os, random
import shutil
import pandas as pd
import numpy as np
import gc

#datetime
import time
from datetime import datetime
from datetime import timedelta
import datetime as dt

import pandas_ta as ta #technical indicators and features
#import ta as ta #Another Technical analysis library - different from professor, but can be installed with conda
from pathlib import Path

# import boruta
from boruta import BorutaPy

# warnings
import warnings
warnings.filterwarnings('ignore')

# visualization - plotting & outputs
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.font_manager
plt.style.use('seaborn')
import cufflinks as cf
cf.set_config_file(offline=True)
import dataframe_image as dfi #Saving pandas dataframes as images
import seaborn as sns

# functions from helper
from src.helper import *

# import custom transformer
#from helper import DayTransformer, TimeTransformer

# sklearn imports
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# metrics
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import plot_confusion_matrix, auc, roc_curve, plot_roc_curve

# import classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.neighbors import KNeighborsClassifier

# tensorflow
import tensorflow as tf
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator 

from tensorflow.keras.optimizers import Adam, RMSprop 
from tensorflow.keras.losses import BinaryCrossentropy 
from tensorflow.keras.metrics import BinaryAccuracy, Accuracy, AUC, Precision, Recall
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from tensorflow.keras.layers import Dropout, Dense, Flatten
from tensorflow.keras.layers import LSTM, BatchNormalization


# kerastuner
import keras_tuner as kt
#from kerastuner import HyperParameter, HyperParameters
#from kerastuner.tuners import RandomSearch, BayesianOptimization, Hyperband

from keras_tuner import HyperParameter, HyperParameters
from keras_tuner.tuners import RandomSearch, BayesianOptimization, Hyperband

