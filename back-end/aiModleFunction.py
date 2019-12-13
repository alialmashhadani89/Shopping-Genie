# Importing the Keras libraries and packages
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout

from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np
import os

def model_create(input_data):
    
    input_data = pd.DataFrame(input_data)

    sc = MinMaxScaler(feature_range=(0, 1))

    # training_set_scaled = sc.fit_transform(training_set)
    training_set_scaled = sc.fit_transform(input_data)

    # Creating a data structure with 60 timesteps and 1 output
    X_train = []
    y_train = []

    for i in range(60, len(training_set_scaled)):
        X_train.append(training_set_scaled[i-60:i, 0])
        y_train.append(training_set_scaled[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)

    # Reshaping
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    
    # Part 2 - Building the RNN
   
    # Initialising the RNN
    regressor = Sequential()

    # Adding the first LSTM layer and some Dropout regularisation
    regressor.add(LSTM(units=50, return_sequences=True,
                       input_shape=(X_train.shape[1], 1)))
    regressor.add(Dropout(0.2))

    # Adding a second LSTM layer and some Dropout regularisation
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))

    # Adding a third LSTM layer and some Dropout regularisation
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))

    # Adding a fourth LSTM layer and some Dropout regularisation
    regressor.add(LSTM(units=50))
    regressor.add(Dropout(0.2))

    # Adding the output layer
    regressor.add(Dense(units=1))

    # Compiling the RNN
    regressor.compile(optimizer='adam', loss='mean_squared_error')

    # if the model is already been computed, then load it
    # else, compute, save it then load it.
    #regressor.fit(X_train, y_train, epochs=100, batch_size=32)

    
    regressor.fit(X_train, y_train, epochs=100, batch_size=32)
    regressor.save('price_prediction.h5')
    