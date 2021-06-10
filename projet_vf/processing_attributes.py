from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np


def process_house_attributes(train, test):
    continuous = [
        "months",
        "day",
        "No disposition",
        "Nombre de lots",
        "Surface reelle bati",
        "Nombre pieces principales",
    ]

    train_continuous = train[continuous]
    test_continuous = test[continuous]

    # put into categorical data the qualitative variables
    categorical = ["Commune", "Type local"]
    encoder = OneHotEncoder(sparse=False)
    train_categorical = encoder.fit_transform(train[categorical])
    test_categorical = encoder.fit_transform(test[categorical])

    train_x = np.hstack([train_categorical, train_continuous])
    test_x = np.hstack([test_categorical, test_continuous])

    # return the concatenated data
    return train_x, test_x


