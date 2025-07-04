import folium
from folium import plugins
from IPython.display import display
import folium.map
import pandas as pd


def plot_cyclone_paths_with_impact(df, region_shapes=None):
    """
    Plots cyclone paths on a map with optional regional impact overlay.

    Parameters:
    - df: DataFrame with columns ['cyclone_name', 'lat', 'lon', 'timestamp']
    - region_shapes: Optional list of tuples (name, geojson_dict, color)

    Displays:
    - folium.Map object
    """
    # Initialize map
    m = folium.Map(location=[20.0, 80.0], zoom_start=4, tiles='cartodb positron')

    # Group by cyclone name to draw paths
    for name, group in df.groupby('cyclone_name'):
        coordinates = group.sort_values('timestamp')[['lat', 'lon']].values.tolist()
        folium.PolyLine(locations=coordinates, tooltip=name, color='blue').add_to(m)
        # Add starting point marker
        start_point = coordinates[0]
        folium.Marker(
            location=start_point,
            tooltip=f"{name} (Start)",
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(m)

    # Add optional regional overlays
    if region_shapes:
        for region_name, geojson_data, color in region_shapes:
            folium.GeoJson(
                geojson_data,
                name=region_name,
                style_function=lambda x, c=color: {'fillColor': c, 'color': c, 'weight': 2, 'fillOpacity': 0.3}
            ).add_to(m)

    # Add layer control if regions exist
    if region_shapes:
        folium.LayerControl().add_to(m)

    # Display map
    m.save('cyclone_paths_with_impact.html')

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
df=pd.DataFrame(data)
plot_cyclone_paths_with_impact(df)