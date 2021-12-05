import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])

map = folium.Map(
    location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain"
)
fg = folium.FeatureGroup(name="My Map")


for lat, lon, ele, nam in zip(latitude, longitude, elevation, name):
    fg.add_child(
        folium.Marker(
            location=[lat, lon],
            popup=f"<strong>{nam}</strong>\n{ele} meters",
            icon=folium.Icon(color="green"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
