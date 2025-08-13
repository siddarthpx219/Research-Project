import pandas as pd

def get_cyclone_data():
    data = pd.read_csv("Research-Project/cyclonedataforResearch.csv")
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df