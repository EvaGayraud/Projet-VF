from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor


def regression(train_x, train_y):
    regr = RandomForestRegressor(n_estimators=1000, max_depth=5, random_state=100)
    regression = regr.fit(train_x, train_y)
    for name, feature in zip(['months', 'day', 'No disposition', 'Nombre de lots', "Surface reelle bati",
                              "Nombre pieces principales", "Code postal", 'Type local',
                              'Section', 'Type de voie'],
                             regression.feature_importances_):
        print(name, round(feature * 100, 1))

    return regression


def knn(train_x, train_y):
    knn = KNeighborsRegressor(n_neighbors=7)
    knn_pred = knn.fit(train_x, train_y)

    return knn_pred
