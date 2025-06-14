import pandas as pd

def get_cyclone_data():
    data = {
        'cyclone_name': ['Fani', 'Amphan', 'Yaas'],
        'landfall_date': ['2019-05-03', '2020-05-20', '2021-05-26'],
        'region': ['Odisha', 'West Bengal', 'Odisha'],
        'intensity': ['Very Severe', 'Super Cyclonic', 'Very Severe']
    }
    df = pd.DataFrame(data)
    df['landfall_date'] = pd.to_datetime(df['landfall_date'])
    return df