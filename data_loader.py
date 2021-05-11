import pandas as pd
from tqdm.notebook import tqdm

url_dict = {
    '2020': 'https://www.data.gouv.fr/fr/datasets/r/90a98de0-f562-4328-aa16-fe0dd1dca60f',
    '2019': 'https://www.data.gouv.fr/fr/datasets/r/3004168d-bec4-44d9-a781-ef16f41856a2',
    '2018': 'https://www.data.gouv.fr/fr/datasets/r/1be77ca5-dc1b-4e50-af2b-0240147e0346',
    '2017': 'https://www.data.gouv.fr/fr/datasets/r/7161c9f2-3d91-4caf-afa2-cfe535807f04',
    '2016': 'https://www.data.gouv.fr/fr/datasets/r/0ab442c5-57d1-4139-92c2-19672336401c',
}


def get_subsample():
    data_all_year = []
    for year, url in tqdm(url_dict.items()):
        data_ = pd.read_csv(url, low_memory=False, sep="|")

        # drop columns based on number of null
        data_ = data_.drop(['Code service CH', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI',
                      '4 Articles CGI', '5 Articles CGI', 'B/T/Q', 'Prefixe de section', 'No Volume', '1er lot',
                      'Surface Carrez du 1er lot', '2eme lot', 'Surface Carrez du 2eme lot', '3eme lot',
                      'Surface Carrez du 3eme lot', '4eme lot', 'Surface Carrez du 4eme lot', '5eme lot',
                      'Surface Carrez du 5eme lot', 'Identifiant local', 'Code voie', 'Code type local',
                      'No Volume', 'Nature culture', 'Nature culture speciale', 'Surface terrain',
                      'No voie', 'Voie', 'No plan'], axis=1)

        data = data_[data_['Code departement'] == '75']
        del data_
        data['year'] = year
        data_all_year.append(data)
        del data

    df = pd.concat(data_all_year)

    return df


def load_house_attributes(df):
    df.drop_duplicates()
    df.dropna(inplace=True)

    # convert to the correct type
    df['Date mutation'] = pd.to_datetime(df['Date mutation'], format='%d/%m/%Y')
    df['year'] = df['Date mutation'].dt.year
    df['months'] = df['Date mutation'].dt.month
    df['day'] = df['Date mutation'].dt.day
    df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',', '.').astype(float)
    df['Nombre pieces principales'] = df['Nombre pieces principales'].astype(int)
    df['Code postal'] = df['Code postal'].astype(str)

    # remove outliers
    df = df[df['Valeur fonciere'] <= 5000000]
    df = df[df['Surface reelle bati'] >= 5]
    df = df[df['Nombre pieces principales'] <= 20]
    df = df[df['Nombre pieces principales'] > 0]

    return df

