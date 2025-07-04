import folium
from folium import plugins


def plot_cyclone_paths_with_impact(df, region_shapes=None):
    """
    Plots cyclone paths on a map with optional regional impact overlay.

    Parameters:
    - df: DataFrame with columns ['cyclone_name', 'lat', 'lon', 'timestamp']
    - region_shapes: Optional list of tuples (name, geojson_dict, color)

    Returns:
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

    return m
