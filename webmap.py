import folium

import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])

lon = list(data["LON"])

elev = list(data["ELEV"])

def color_producer(elevation):
	if el < 1000:
		return 'green'
	elif 1000<=el<=3000:
		return 'orange'
	else:
		return 'red'

map = folium.Map(location=[34.65, -99.03], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="World Map")

for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup= str(el)+" m", fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data=open("world.json", 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000}))

map.add_child(fg)

map.save("Map1.html")
