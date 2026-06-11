import requests

response = requests.get("https://nominatim.openstreetmap.org")
print(response.status_code)

from geopy.geocoders import Nominatim

geolocator = Nominatim(
    user_agent="weather-etl-project"
)

location = geolocator.reverse("22.601053, 88.31776")

print(location)