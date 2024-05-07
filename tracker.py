import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
ph_1=phonenumbers.parse("+917894967606")
print("\nphone numbers location\n")
loc=(geocoder.description_for_number(ph_1,"en"))
print(loc)

#carrier name

from phonenumbers import carrier
print(carrier.name_for_number(ph_1,"en"))

from opencage.geocoder import OpenCageGeocode
key="c5f57edf805f4698b0dee41863969006"
geocoder= OpenCageGeocode(key)
query=str(loc)
res=(geocoder.geocode(query))
lat=res[0]['geometry']['lat']
lng=res[0]['geometry']['lng']
print(lat,lng)

myMap= folium.Map(loc=[lat,lng], zoom_start= 9)
folium.Marker([lat, lng], popup=loc).add_to(myMap)

myMap.save("mylocation.html")
