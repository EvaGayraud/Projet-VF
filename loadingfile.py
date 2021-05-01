"""Prédire la Valeur fonciere du bien avec les critères suivants : type local, code postal,
Nombre pieces principales et Surface reelle bati, montrer les résultats sur un graphique
grâce à Plotly"""

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import plotly.express as px


def load_house_attributes(file):
    # get the dataframe
    cols = ['Valeur fonciere', 'Surface reelle bati', 'Nombre pieces principales',
            'Type local', 'Commune']
    df0 = pd.read_csv(file, usecols=cols, low_memory=False, sep="|")
    df = df0.copy()

    df['Type local'].replace('', np.nan, inplace=True)
    df.dropna(inplace=True)

    Arrondissements_Paris = ['PARIS 01', 'PARIS 02', 'PARIS 03', 'PARIS 04', 'PARIS 05',
                             'PARIS 06', 'PARIS 07', 'PARIS 08', 'PARIS 09', 'PARIS 10',
                             'PARIS 11', 'PARIS 12', 'PARIS 13', 'PARIS 14', 'PARIS 15',
                             'PARIS 16', 'PARIS 17', 'PARIS 18', 'PARIS 19', 'PARIS 20']
    df_paris = df[df['Commune'].isin(Arrondissements_Paris)]
    df_paris = df_paris.drop_duplicates()
    df_paris['Valeur fonciere'] = df_paris['Valeur fonciere'].str.replace(',', '.')

    # remove outliers
    df_paris['Valeur fonciere'] = df_paris['Valeur fonciere'].astype(float)
    df_paris['Valeur fonciere'] = df_paris[df_paris['Valeur fonciere'] < 100000000]
    df_paris = df_paris[df_paris['Surface reelle bati'] >= 10]
    df_paris['Code postal'] = df_paris['Code postal'].astype(str)
    df_paris['Nombre pieces principales'] = df_paris['Nombre pieces principales'].astype(int)
    df_paris = df_paris[df_paris['Nombre pieces principales'] <= 20]

    fig = px.box(df_paris, x='Valeur fonciere', y='Code postal', hover_name='Type local')
    #fig.show()

    return df_paris


def process_house_attributes(df_paris, train, test):

    # we would like to exploit both continuous and categorical variables
    continuous = ["Surface reelle bati", "Nombre pieces principales"]
    cs = MinMaxScaler()

    trainContinuous = cs.fit_transform(train[continuous])
    testContinuous = cs.transform(test[continuous])

    # put into categorical data the qualitative variables
    CategoricalBin = OrdinalEncoder().fit_transform(df_paris["Code postal"], df_paris["Type Local"])
    trainCategorical = CategoricalBin.transform(train["Code postal"], train["Type Local"])
    testCategorical = CategoricalBin.transform(test["Code postal"], test["Type Local"])

    # construct and concatenate the training and testing categorical and continuous dataset
    trainX = np.hstack([trainCategorical, trainContinuous])
    testX = np.hstack([testCategorical, testContinuous])

    # return the concatenated training and testing data
    return trainX, testX

load_house_attributes('valeursfoncieres-2020.txt')
