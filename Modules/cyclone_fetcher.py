import pandas as pd

def get_cyclone_data():
    data = pd.read_csv("d:/researchWork/Research-Project/ResearchProjectcyclones.csv")
    df = pd.DataFrame(data)
    df['Landfall_Date'] = pd.to_datetime(df['Landfall_Date'])
    return df