import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])
html = """
<div class="container" style="font-family:sans-serif;">
<a href="https://www.google.com/search?q=%%22%s%%22%%20volcano" target="_blank"><strong>%s</strong></a><br />
Height: %s m
</div>
"""


def set_color(elevation):
    if elevation > 3000:
        return "red"
    elif 2000 < elevation < 3000:
        return "orange"

    return "green"


map = folium.Map(
    location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain"
)
fg = folium.FeatureGroup(name="My Map")


for lat, lon, ele, nam in zip(latitude, longitude, elevation, name):
    iframe = folium.IFrame(html=html % (nam, nam, ele), width=200, height=100)
    fg.add_child(
        # folium.Marker(
        #     location=[lat, lon],
        #     popup=folium.Popup(iframe),
        #     icon=folium.Icon(color=set_color(ele)),
        # )
        folium.CircleMarker(
            location=[lat, lon],
            popup=folium.Popup(iframe),
            color=set_color(ele),
            fill_color=set_color(ele),
            fill=True,
            fill_opacity=0.5,
            radius=10,
        )
    )

fg.add_child(
    folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()))
)

map.add_child(fg)
map.save("Map1.html")
