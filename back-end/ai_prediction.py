# Recurrent Neural Network


# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import pandas as pd


# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
from aiModleFunction import model_create
from tensorflow.keras.models import load_model


def get_predication(input_data, future_prices):

    input_data = pd.DataFrame(input_data)

    sc = MinMaxScaler(feature_range=(0, 1))

    # training_set_scaled = sc.fit_transform(training_set)
    training_set_scaled = sc.fit_transform(input_data)

    # Creating a data structure with 60 timesteps and 1 output
    X_train = []
    y_train = []

    for i in range(40, len(training_set_scaled)):
        X_train.append(training_set_scaled[i-40:i, 0])
        y_train.append(training_set_scaled[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)

    # Reshaping
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    
    # create the model. 
    # will be active when it needed.
    #model_create(X_train,y_train)
    
    # loading the model.
    regressor = load_model('price_prediction.h5')

    # Part 3 - Making the predictions

    # Getting the prices to work with for the next 10 days.
    future_predication = pd.DataFrame(future_prices)

    # formating the prices so we can start the predication
    dataset_total = pd.concat((input_data, future_predication), axis=0)
    inputs = dataset_total[len(dataset_total) -
                           len(future_predication) - 40:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)
    X_test = [] 

    # reshaping the data
    for i in range(40, len(inputs)):
        X_test.append(inputs[i-40:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_price = regressor.predict(X_test)

    # where is the final price will be
    predicted_price = sc.inverse_transform(predicted_price)
    return str(float(' '.join(map(str, predicted_price[len(predicted_price)-1]))))

# the main function inside the ai
# the main function has all the data for each store
# we will do at most 4 ai predication and atless one


def get_redication_price(pricesdb, future_prices):
    store_list = ['Best Buy', 'Amazon', 'B&H', "Walmart"]
    predication_list = {}
    if (len(pricesdb) == 0):
        predication_list = ['0'] * 4

    else:
        training_set = pd.DataFrame(pricesdb)

        for store in store_list:
            data = training_set[training_set[1] == store]
            if (len(data) >= 40):
                predication_list.update(
                    {store: get_predication((data[0]), future_prices)})
            else:
                predication_list.update({store: '0'})

    return predication_list
