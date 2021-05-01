"""Prédire la Valeur fonciere du bien avec les critères suivants : type local, code postal,
Nombre pieces principales et Surface reelle bati, montrer les résultats sur un graphique"""

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
from matplotlib.ticker import AutoMinorLocator
from sklearn import preprocessing
from keras.utils import to_categorical

ax1 = sns.violinplot("Type local", "Valeur fonciere", data=df, hue='Type local')
ax1.minorticks_on()
ax1.xaxis.set_minor_locator(AutoMinorLocator(2))
ax1.grid(which='minor', axis='x', linewidth=1)

x = df.drop('Valeur fonciere', axis=1)
y = df['Valeur fonciere']
# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'species'.
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

lr = LinearRegression()
lr_baseline = lr.fit(xtrain[["Surface reelle bati"]], ytrain)
baseline_pred = lr_baseline.predict(xtest[["Surface reelle bati"]])
