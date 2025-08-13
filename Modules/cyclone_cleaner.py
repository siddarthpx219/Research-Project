import pandas as pd

def clean_cyclone_data(df):
    #df['region'] = df['region'].str.title()
    df['Intensity'] = df['intensity'].map({
        'TS':1,
        'CS':2,
        'SCS':3,
        'VSCS':4,
        'SuCS':5
    })
    return df