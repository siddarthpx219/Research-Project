import pandas as pd

def clean_cyclone_data(df):
    df['region'] = df['region'].str.title()
    df['intensity_score'] = df['intensity'].map({
        'Depression': 1,
        'Deep Depression': 2,
        'Cyclonic Storm': 3,
        'Severe Cyclonic Storm': 4,
        'Very Severe': 5,
        'Extremely Severe': 6,
        'Super Cyclonic': 7
    })
    return df