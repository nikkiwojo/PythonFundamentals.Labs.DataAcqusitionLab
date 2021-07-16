
import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv() # loads api key from .env file

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1000&offset={offset}"
headers = {'token': os.getenv('token')}
offset_count = 1
json_count = 0

while json_count <= 39:
    requesting = urllib.request.Request(url.format(offset = offset_count), headers = headers)
    with urllib.request.urlopen(requesting) as y:
        bites = y.read()
        new_var = json.loads(bites)
        with open(f"locations_{json_count}.json", "w") as file:
            json.dump(new_var, file, indent = 4)
    json_count += 1
    offset_count += 1000