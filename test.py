import numpy as np
from data_loader import load_house_attributes
from sklearn.model_selection import train_test_split
from processing_attributes import process_house_attributes
from model import regression
from model import knn


"""
df_paris = load_house_attributes('https://www.data.gouv.fr/fr/datasets/r/90a98de0-f562-4328-aa16-fe0dd1dca60f')
train, test = train_test_split(df_paris, test_size=0.25, random_state=42)

train_x, test_x = process_house_attributes(df_paris, train, test)
train_y = train["Valeur fonciere"]
test_y = test["Valeur fonciere"]

prediction_regr = regression(train_x, train_y)
prediction_knn = knn(train_x, train_y)

errors_regr = abs(prediction_regr - test_y)
errors_knn = abs(prediction_knn - test_y)
print('Mean Absolute Error regr:', round(np.mean(errors_regr), 2), 'euros.')
print('Mean Absolute Error knn:', round(np.mean(errors_knn), 2), 'euros.')
"""
"""attributes = {'Surface reelle bati': [20],
              'Nombre de piece principales': [1],
              'Type local': ['Appartement'],
             'Code postal': ['75018']}

df_input = pd.DataFrame(attributes)

from inputs import process_attributes

attr = process_attributes(df_input)
"""
"""prediction_knn = knn.predict(attr)
print(prediction_knn)
prediction_regr = regr.predict(attr)
print(prediction_regr)

votre_estimation = prediction_knn.tolist()
estimation = round(np.mean(votre_estimation), 2)
print(estimation)"""

"""plt.figure(figsize=(12,8))
plt.plot(test_y, color='red')
plt.plot(pred_regr, color='blue')
plt.show()
"""