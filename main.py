from geopy.geocoders import Nominatim

Geolocater = Nominatim(user_agent="GeoLocation")

Location = Geolocater.geocode("Jakarta")

print("Address: ", Location.address)
print("Latitude: ", Location.latitude)
print("Longitude", Location.longitude)