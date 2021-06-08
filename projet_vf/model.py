from sklearn.ensemble import RandomForestRegressor


def regression(train_x, train_y):

    regr = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=100)
    regression = regr.fit(train_x, train_y)
    return regression

