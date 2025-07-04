import pandas as pd

def get_cyclone_data():
    #data = pd.read_csv("/Users/siddarth/Downloads/Research/Research-Project/ResearchProjectcyclones.csv")
    data = [
    {"cyclone_name": "Nargis", "lat": 16.8, "lon": 94.8, "timestamp": "2008-05-02"},
    {"cyclone_name": "Phailin", "lat": 19.2, "lon": 84.8, "timestamp": "2013-10-12"},
    {"cyclone_name": "Hudhud", "lat": 17.7, "lon": 83.3, "timestamp": "2014-10-12"},
    {"cyclone_name": "Roanu", "lat": 15.3, "lon": 80.1, "timestamp": "2016-05-21"},
    {"cyclone_name": "Vardah", "lat": 13.1, "lon": 80.3, "timestamp": "2016-12-12"},
    {"cyclone_name": "Fani", "lat": 19.8, "lon": 85.7, "timestamp": "2019-05-03"},
    {"cyclone_name": "Bulbul", "lat": 21.6, "lon": 88.3, "timestamp": "2019-11-05"},
    {"cyclone_name": "Amphan", "lat": 21.4, "lon": 87.8, "timestamp": "2020-05-20"},
    {"cyclone_name": "Nivar", "lat": 12.0, "lon": 79.8, "timestamp": "2020-11-23"},
    {"cyclone_name": "Yaas", "lat": 21.9, "lon": 87.1, "timestamp": "2021-05-26"},
    {"cyclone_name": "Asani", "lat": 15.5, "lon": 81.3, "timestamp": "2022-05-11"},
    {"cyclone_name": "Mocha", "lat": 19.0, "lon": 92.8, "timestamp": "2023-05-14"},
    {"cyclone_name": "Remal", "lat": 21.9, "lon": 89.1, "timestamp": "2024-05-26"},
]
    df = pd.DataFrame(data)
    df['Landfall_Date'] = pd.to_datetime(df['Landfall_Date'])
    return df