from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def process_house_attributes(df, train, test):
    # we would like to exploit continuous data from 0 to 1
    continuous = ["Surface reelle bati", "Nombre pieces principales"]
    cs = MinMaxScaler()
    trainContinuous = cs.fit_transform(train[continuous])
    testContinuous = cs.transform(test[continuous])

    # put into categorical data the qualitative variables
    categorical = ["Type local", "Code postal"]
    ord_enc = OrdinalEncoder()
    CategoricalBin = ord_enc.fit(df[categorical])
    trainCategorical = CategoricalBin.transform(train[categorical])
    testCategorical = CategoricalBin.transform(test[categorical])

    # construct and concatenate the training and testing categorical and continuous dataset
    train_x = np.hstack([trainCategorical, trainContinuous])

    test_x = np.hstack([testCategorical, testContinuous])

    # return the concatenated data
    return train_x, test_x