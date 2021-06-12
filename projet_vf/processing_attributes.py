from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
import numpy as np
from sklearn.pipeline import Pipeline


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

    pipeline_cat = Pipeline([('onehotencode', OneHotEncoder(sparse=False)),
                             ('reductor', PCA())
                             ])

    train_categorical = pipeline_cat.fit_transform(train[categorical])
    test_categorical = pipeline_cat.fit_transform(test[categorical])

    train_x = np.hstack([train_categorical, train_continuous])
    test_x = np.hstack([test_categorical, test_continuous])

    # return the concatenated data
    return train_x, test_x
