from statsmodels.tsa.stattools import grangercausalitytests

def run_granger(df, maxlag=5):
    result = grangercausalitytests(df, maxlag=maxlag, verbose=False)
    return result
