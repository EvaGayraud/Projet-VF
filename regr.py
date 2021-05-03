from sklearn.ensemble import RandomForestRegressor


def regression(train_x, train_y):

    regr = RandomForestRegressor(max_depth=5, random_state=0)
    regression = regr.fit(train_x, train_y)

    return regression