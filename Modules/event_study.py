import numpy as np

def compute_ar_car(df, market_return):
    df['AR'] = df['Log_Return'] - market_return
    df['CAR'] = df['AR'].cumsum()
    return df
