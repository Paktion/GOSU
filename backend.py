import googlemaps
import requests
import json
import urllib

# importing googlemaps module
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBPc6V-4zZu_Xg7UGUoQVSImQX8-oN-C40')  

placeid = "Dreese Lab"

url = "https://www.google.com/maps/search/?api=1&query=Google&query_place_id=" + placeid

geocode_result = gmaps.reverse_geocode(url)
print(geocode_result)

# #source and destination coordinate pairs being stores 
# origin_latitude = 12.9551779
# origin_longitude = 77.6910334
# destination_latitude = 28.505278
# destination_longitude = 77.327774

# #uses the distance_matrix function to get the distance between the coordinate pairs
# distance = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)], [str(destination_latitude) + " " + str(destination_longitude)], mode='walking')['rows'][0]['elements'][0]

# print(distance)
