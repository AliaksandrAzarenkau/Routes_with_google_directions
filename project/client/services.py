import datetime

import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()
g_key = os.getenv("GOOGLE_API_KEY")
gmaps = googlemaps.Client(g_key)


def get_latlon(address):
    geocode_result = gmaps.geocode(f'{address[0]}, {address[1]}, {address[2]}, {address[3]}')
    latlon = [
        geocode_result[0]['geometry']['location']['lat'],
        geocode_result[0]['geometry']['location']['lng']
    ]
    return latlon
