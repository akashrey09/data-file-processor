import pandas as pd

def load_csv(filepath):
    df = pd.read_csv(filepath)
    return df

def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    removed = before-len(df)
    return df, removed

def handle_missing(df,strategy):
    if strategy=='drop':
        df = df.dropna()
        return df
    if strategy=='mean':
        df = df.fillna(df.mean(numeric_only=True))
        return df
    if strategy=='mode':
        df = df.fillna(df.mode().iloc[0])
        return df