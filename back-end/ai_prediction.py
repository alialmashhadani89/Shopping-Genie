# Recurrent Neural Network


# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler

# Importing the Keras libraries and packages
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout


def get_redication_price(pricesdb, future_prices):

    training_set = pd.DataFrame(pricesdb)

    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)
    # Creating a data structure with 60 timesteps and 1 output
    X_train = []
    y_train = []

    for i in range(10, len(training_set_scaled)):
        X_train.append(training_set_scaled[i-10:i, 0])
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
    if(not os.path.exists('price_prediction.h5')):
        regressor.fit(X_train, y_train, epochs=100, batch_size=32)
        regressor.save('price_prediction.h5')

    regressor = load_model('price_prediction.h5')

    # Part 3 - Making the predictions

    # Getting the prices to work with for the next 10 days.
    future_predication = pd.DataFrame(future_prices)

    # formating the prices so we can start the predication
    dataset_total = pd.concat((training_set, future_predication), axis=0)
    inputs = dataset_total[len(dataset_total) -
                           len(future_predication) - 10:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)
    X_test = []

    for i in range(10, len(inputs)):
        X_test.append(inputs[i-10:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_price = regressor.predict(X_test)

    # where is the final price will be
    predicted_price = sc.inverse_transform(predicted_price)
    return predicted_price[len(predicted_price)-1]
