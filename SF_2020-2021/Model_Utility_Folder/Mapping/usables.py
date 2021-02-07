import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import descartes
from shapely.geometry import Point
import os

# Reading and taking the lat. and long. of unique locaitons
cities = pd.read_csv("SF/SF_2020-2021/Data/FilteredEcon.csv")
locations = cities[["Municipality", "Latitude", "Longitude"]]
uniques = locations.drop_duplicates(subset=["Municipality"])
uniques.to_csv("SF/SF_2020-2021/Data/Usables.csv", index=0)

# Setting up .shp map of Canada
map = gpd.read_file(
    "SF/SF_2020-2021/Model_Utility_Folder/Mapping/Shapefile/gpr_000b11a_e.shp")
fig, ax = plt.subplots(figsize=(30, 30))

# Creating location points
points = pd.read_csv("SF/SF_2020-2021/Data/Usables.csv")
crs = {"init": "epsg:4326"}

geometry = [Point(xy) for xy in zip(points["Longitude"], points["Latitude"])]
# Changing Pandas DataFrame into geoDataFrame
geo_df = gpd.GeoDataFrame(points, crs=crs, geometry=geometry)

# Creating final map
map.plot(ax=ax, alpha=0.4, color="grey")
geo_df.plot(ax=ax, markersize=1, color="blue")
plt.show()
