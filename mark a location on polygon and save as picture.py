#!/usr/bin/env python

import cv2
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point

# sample long lat
long=[78.971365]
lat=[20.601992]

#picture name saved as .png format in directory
filename = 'C:\\Users\\Desktop\\saved.png'

#read shapefile
delhi_map = gpd.read_file(r'C:\\Users\\Desktop\\grid.geojson') # put path to shapefile 

#figure plot
fig,ax = plt.subplots(figsize = (15,15))
delhi_map.plot(ax = ax)
geometry = [Point(xy) for xy in zip(long,lat)]
geo_df = gpd.GeoDataFrame(geometry = geometry)
print(geo_df)
g = geo_df.plot(ax = ax, markersize = 90, color = 'yellow',marker = '*')
plt.show()

#saving figure
fig.savefig(filename,bbox_inches='tight')







