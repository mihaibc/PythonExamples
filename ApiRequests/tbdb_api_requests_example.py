import requests
import json
import api_informations as api_info # this is used to not expose the api key

def json_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "api_key" : api_info.api_key,
    "language" : "en-US",
}

response = requests.get("https://api.themoviedb.org/3/discover/movie", params=parameters)
json_print(response.json())


