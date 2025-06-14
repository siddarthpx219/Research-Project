import folium

def plot_cyclone_map(df):
    m = folium.Map(location=[20.0, 80.0], zoom_start=4)
    for _, row in df.iterrows():
        folium.Marker([row['lat'], row['lon']], tooltip=row['cyclone_name']).add_to(m)
    return m