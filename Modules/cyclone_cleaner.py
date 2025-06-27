import pandas as pd

def clean_cyclone_data(df):
    #df['region'] = df['region'].str.title()
    df['intensity_score'] = df['Intensity'].map({
        'Tropical Storm':1,
        'Cyclonic Storm':2,
        'Severe Cyclonic Storm':3,
        'Very Severe Cyclonic Storm':4,
        'Super Cyclonic Storm':5
    })
    return df