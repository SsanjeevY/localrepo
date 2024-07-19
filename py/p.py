import requests

API_KEY = 'AIzaSyC-_2Xo2qDxgAGnkFjAHHLp1u116M27HA4'

# Step 1: Find the Place ID
place_name = 'VasyERP Solutions Pvt. Ltd.'
find_place_url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&key={API_KEY}'
response = requests.get(find_place_url)
place_id = response.json()['candidates'][0]['place_id']

# Step 2: Get Place Details
details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=rating,reviews&key={API_KEY}'
details_response = requests.get(details_url)
place_details = details_response.json()

print("Rating:", place_id)