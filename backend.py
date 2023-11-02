import googlemaps
import requests
import json

# importing googlemaps module
import googlemaps
 
# Requires API key
gmaps = googlemaps.Client(key='AIzaSyBPc6V-4zZu_Xg7UGUoQVSImQX8-oN-C40')
 
# Requires cities name
my_dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]
 
# Printing the result
print(my_dist)