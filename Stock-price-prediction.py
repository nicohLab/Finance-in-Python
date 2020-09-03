import tensorflow as tf 
import math
import pandas_datareader as web
import numpy as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# from sklearn.preprocessing import MinMaxScaler
# from tf.keras.models import Sequential
# from tf.keras.layer import Dense, LSTM
# Get the stock 
df = web.DataReader('TSLA', data_source='yahoo', start='2012-01-01', end='2019-12-31')
print(df )