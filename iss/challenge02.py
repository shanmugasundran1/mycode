import requests
from datetime import datetime
import reverse_geocoder as geocoder

URL = "http://api.open-notify.org/iss-now.json"


tracker = requests.get(URL)

trackerJson = tracker.json()

trackerLocation = trackerJson['iss_position']

lat = trackerLocation["latitude"]
lon = trackerLocation["longitude"]
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

physical_location = geocoder.search((lat, lon))

# slice that object to return the city name only
city= physical_location[0]["name"]

# slice the object again to return the country
country= physical_location[0]["cc"]

print("CURRENT LOCATION OF THE ISS:")
print(f'Latitude: {lat}')
print(f'Longitude: {lon}')
print(f'Current Date and Time: {dt_string}')
print(f'City/Country: {city}, {country}')
