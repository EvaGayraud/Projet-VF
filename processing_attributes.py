from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def process_house_attributes(df, train, test):
    # we would like to exploit continuous data from 0 to 1
    continuous = [
        'months',
        'day',
        'No disposition',
        'Nombre de lots',
        'Surface reelle bati',
        'Nombre pieces principales'
    ]
    cs = MinMaxScaler()
    train_continuous = cs.fit_transform(train[continuous])
    test_continuous = cs.transform(test[continuous])

    # put into categorical data the qualitative variables
    categorical = ["Code postal", 'Type local', 'Section', 'Type de voie']
    ord_enc = OrdinalEncoder()
    categorical_bin = ord_enc.fit(df[categorical])
    train_categorical = categorical_bin.transform(train[categorical])
    test_categorical = categorical_bin.transform(test[categorical])

    # construct and concatenate the training and testing categorical and continuous dataset
    train_x = np.hstack([train_categorical, train_continuous])
    test_x = np.hstack([test_categorical, test_continuous])

    # return the concatenated data
    return train_x, test_x
