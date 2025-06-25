import pandas as pd

def get_cyclone_data():
    data = pd.read_csv("DataCSV/ResearchProjectcyclones.csv")
    df = pd.DataFrame(data)
    df['landfall_date'] = pd.to_datetime(df['landfall_date'])
    return df