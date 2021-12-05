import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])
html = """
<div class="container" style="font-family:sans-serif;">
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank"><strong>%s</strong></a><br />
Height: %s m
</div>
"""

map = folium.Map(
    location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain"
)
fg = folium.FeatureGroup(name="My Map")


for lat, lon, ele, nam in zip(latitude, longitude, elevation, name):
    iframe = folium.IFrame(html=html % (nam, nam, ele), width=200, height=100)
    fg.add_child(
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(iframe),
            icon=folium.Icon(color="green"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
