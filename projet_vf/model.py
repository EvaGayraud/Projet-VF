from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def regression(train_x, train_y):
    pipeline_randomforest = Pipeline([('scalar1', StandardScaler()),
                                      ('rf_classifier',
                                       RandomForestRegressor(n_estimators=200, max_depth=5, random_state=100))])
    regression = pipeline_randomforest.fit(train_x, train_y)

    return regression

