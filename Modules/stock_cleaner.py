import numpy as np

def compute_returns(df):
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
    return df.dropna()
