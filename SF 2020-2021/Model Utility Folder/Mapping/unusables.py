import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import descartes
from shapely.geometry import Point
import numpy as np

data = pd.read_csv("SF/SF 2020-2021/Data/UnusablesCoord.csv")
locations = data[["Municipality", "Longitude", "Latitude"]]
uniques = locations.drop_duplicates(subset=["Municipality"])
uniques.to_csv("SF/SF 2020-2021/Data/UniqueUnusables.csv")

map = gpd.read_file("SF/SF 2020-2021/Model Utility Folder/Mapping/Shapefile/gpr_000b11a_e.shp")
fig, ax = plt.subplots(figsize=(30, 30))

points = pd.read_csv("SF/SF 2020-2021/Data/UniqueUnusables.csv")
crs = {"init": "epsg:4326"}
geometry = [Point(xy) for xy in zip(points["Longitude"], points["Latitude"])]

geo_df = gpd.GeoDataFrame(points, crs=crs, geometry=geometry)

map.plot(ax=ax, alpha=0.4, color="grey")
geo_df.plot(ax=ax, markersize=5, color="red")
plt.show()
