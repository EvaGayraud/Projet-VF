import pandas as pd


def load_house_attributes(url):
    # get the dataframe
    df0 = pd.read_csv(url, low_memory=False, sep="|")
    df = df0.copy()
    df = df[df['Code departement'] == '75']

    # drop columns based on number of null
    df = df.drop(['Code service CH', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI',
                  '4 Articles CGI', '5 Articles CGI', 'B/T/Q', 'Prefixe de section',  'No Volume', '1er lot',
                  'Surface Carrez du 1er lot', '2eme lot', 'Surface Carrez du 2eme lot', '3eme lot',
                  'Surface Carrez du 3eme lot', '4eme lot', 'Surface Carrez du 4eme lot', '5eme lot',
                  'Surface Carrez du 5eme lot',  'Identifiant local', 'Code voie', 'Code type local',
                  'No Volume',  'Nature culture', 'Nature culture speciale', 'Surface terrain',
                  'No voie', 'Voie', 'No plan'], axis=1)

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

