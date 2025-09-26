# preprocessing.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def preprocess_data(df, method="zscore"):
    df = df.dropna()
    if method == "minmax":
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    return df
