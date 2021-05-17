import requests
import json

response = requests.get("https://restcountries.eu/rest/v2/all")

countries = json.loads(response.text)

json_dump = json.dumps(countries)

with open("countries.json", "w") as data_file:
    data_file.write(json_dump)