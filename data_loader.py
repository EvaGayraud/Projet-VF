import pandas as pd
import numpy as np


def load_house_attributes(url):
    # get the dataframe
    cols = ['Valeur fonciere', 'Surface reelle bati', 'Nombre pieces principales',
            'Type local', 'Commune', 'Code postal', 'Code departement']
    df0 = pd.read_csv(url, usecols=cols, low_memory=False, sep="|")
    df = df0.copy()

    df['Type local'].replace('', np.nan, inplace=True)
    df.dropna(inplace=True)

    df_paris = df[df['Code departement'] == '75']
    df_paris = df_paris.drop_duplicates()
    df_paris['Valeur fonciere'] = df_paris['Valeur fonciere'].str.replace(',', '.')

    # convert to the correct type
    df_paris['Valeur fonciere'] = df_paris['Valeur fonciere'].astype(float)
    df_paris['Code postal'] = df_paris['Code postal'].astype(str)
    df_paris['Nombre pieces principales'] = df_paris['Nombre pieces principales'].astype(int)

    # remove outliers
    df_paris = df_paris[df_paris['Valeur fonciere'] <= 1000000000]
    df_paris = df_paris[df_paris['Surface reelle bati'] >= 10]
    df_paris = df_paris[df_paris['Nombre pieces principales'] <= 20]
    df_paris = df_paris[df_paris['Nombre pieces principales'] > 0]


    return df_paris



