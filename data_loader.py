import pandas as pd
import numpy as np


def load_house_attributes(url):
    # get the dataframe
    cols = ['Valeur fonciere', 'Surface reelle bati', 'Nombre pieces principales',
            'Type local', 'Commune', 'Code postal', 'Code departement']
    df0 = pd.read_csv(url, usecols=cols, low_memory=False, sep="|")
    df = df0.copy()
    
    df.drop_duplicates()
    df.dropna(inplace=True)
    df = df[df['Code departement'] == '75']

    # convert to the correct type
    df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',', '.').astype(float)
    df['Code postal'] = df['Code postal'].astype(str)
    df['Nombre pieces principales'] = df['Nombre pieces principales'].astype(int)

    # remove outliers
    df = df[df['Valeur fonciere'] <= 10000000]
    df = df[df['Surface reelle bati'] >= 5]
    df = df[df['Nombre pieces principales'] <= 20]
    df = df[df['Nombre pieces principales'] > 0]

    return df
