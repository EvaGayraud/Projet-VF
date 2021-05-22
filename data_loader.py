import pandas as pd


def load_house_attributes(df):
    df.drop_duplicates()
    df.dropna(inplace=True)
    pd.options.mode.chained_assignment = None
    df = df[df['Type local'].isin(['Maison', 'Appartement'])]
    df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',', '.').astype(float)

    df = auto_type_columns(df)
    df = post_treatment_columns(df)

    # remove outliers
    df = df[df['Valeur fonciere'] <= 5000000]
    df = df[df['Surface reelle bati'] < 300]
    df = df[df['Nombre pieces principales'] <= 10]

    return df


def auto_type_columns(df):
    for column in df.columns:
        value = df[column].iloc[0]
        type_value = type(value)
        df[column] = df[column].astype(type_value)

    return df


def post_treatment_columns(df):
    df['Date mutation'] = pd.to_datetime(df['Date mutation'], format='%d/%m/%Y')
    df['year'] = df['Date mutation'].dt.year
    df['months'] = df['Date mutation'].dt.month
    df['day'] = df['Date mutation'].dt.day

    return df
