import geocoder
import requests


destinations = [
'Space Needle',
'Crater Lake',
'Golden Gate Bridge',
'Yosemite National Park',
'Las Vegas, Nevada',
'Grand Canyon National Park',
'Aspen, Colorado',
'Mount Rushmore',
'Yellowstone National Park',
'Sandpoint, Idaho',
'Banff National Park',
'Capilano Suspension Bridge',
]


with open("DarkSkyKey.txt","r") as mykey:
	api_key = mykey.read()

api_url_base = "https://api.darksky.net/forecast/"+api_key+"/"

def get_api_url(location):
	latitude = str(format(geocoder.arcgis(location).lat,'.4f'))
	longitude = str(format(geocoder.arcgis(location).lng,'.4f'))
	full_api_url = api_url_base+latitude+","+longitude
	return full_api_url

for place in destinations:
	latitude = str(format(geocoder.arcgis(place).lat,'.4f'))
	longitude = str(format(geocoder.arcgis(place).lng,'.4f'))
	latlong = (latitude,longitude)
	result = requests.get(get_api_url(place))
	weather = result.json()
	summary = weather['currently']['summary']
	temperature = "{0:.1f}".format(weather['currently']['temperature'])
	sentence = ("The {0} is located at {1} \n At {0} right now,"
	" it's {2} with a temperature of {3}\u00B0F").format(place,latlong,summary,temperature)
	print(sentence)


