import pandas as pd
import folium

df = pd.read_csv("sensorenregister_gemeente_Groningen.csv", delimiter=";")

# Filter for CCTV only
df = df[df["typesensor"] == "Cameratoezicht"]

tiles_list = [
    'CartoDB positron',
    'CartoDB dark_matter',
    'CartoDB Voyager',
]

# Create map centered on the average location
m = folium.Map(location=[df["lat"].mean(), df["lon"].mean()], zoom_start=17)

# Add markers for each camera
for _, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        icon=folium.CustomIcon("camera_icon.png", icon_size=(50, 50)),
    ).add_to(m)

for tile in tiles_list:
    folium.TileLayer(tile, name=tile).add_to(m)
folium.LayerControl().add_to(m)

m.save("cameras_map.html")