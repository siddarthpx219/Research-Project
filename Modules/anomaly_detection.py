from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[['Log_Return']])
    return df