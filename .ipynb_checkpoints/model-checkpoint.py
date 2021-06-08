from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import data_loader


def train_test(df):

    (train, test) = train_test_split(df, test_size=0.25, random_state=42)

    return train, test


def train_test_x_y(df, train, test):

    max_price = train["Valeur fonciere"].max()
    train_y = train["Valeur fonciere"] / max_price
    test_y = test["Valeur fonciere"] / max_price

    (train_x, test_x) = data_loader.process_house_attributes(df, train, test)

    return train_x, test_x, train_y, test_y


def model(train_x, train_y):
    regr = RandomForestRegressor(max_depth=5, random_state=0)

    regression = regr.fit(train_x, train_y)

    return regression
