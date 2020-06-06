import http.client
import mimetypes
import json
import os
key = os.getenv('weather_api')
conn = http.client.HTTPSConnection("dataservice.accuweather.com")


def city_id(city):
    payload = ''
    headers = {}

    link = "/locations/v1/cities/search?apikey="
    citylink = link + key + "&q=" + city
    conn.request("GET", citylink, payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    return str(data[0]["Key"])