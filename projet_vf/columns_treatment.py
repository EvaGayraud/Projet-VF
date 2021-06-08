import pandas as pd


def auto_type_columns(df):
    for column in df.columns:
        value = df[column].iloc[0]
        type_value = type(value)
        df[column] = df[column].astype(type_value)

    return df


def post_treatment_columns(df):
    df["Date mutation"] = pd.to_datetime(df["Date mutation"], format="%d/%m/%Y")
    df["year"] = df["Date mutation"].dt.year
    df["months"] = df["Date mutation"].dt.month
    df["day"] = df["Date mutation"].dt.day

    return df
