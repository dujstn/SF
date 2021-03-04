import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import descartes
import os
from shapely.geometry import Point

data = pd.read_csv("SF_2020-2021/Data/UniqueUnusableInso.csv")
dataTwo = pd.read_csv("SF_2020-2021/Data/Usables.csv")
locations = data[["Municipality", "Longitude", "Latitude"]]
locationsTwo = dataTwo[["Municipality", "Longitude", "Latitude"]]
uniquesOne = locations.drop_duplicates(subset=["Municipality"])
uniquesTwo = locationsTwo.drop_duplicates(subset=["Municipality"])
uniques = uniquesOne.append(uniquesTwo)
uniques.to_csv("SF_2020-2021/Data/AllInso.csv", index=0)



map = gpd.read_file(
    "SF_2020-2021/Model_Utility_Folder/Mapping/Shapefile/gpr_000b11a_e.shp")
fig, ax = plt.subplots(figsize=(30, 30))

points = pd.read_csv("SF_2020-2021/Data/AllInso.csv")
crs = {"init": "epsg:4326"}
geometry = [Point(xy) for xy in zip(points["Longitude"], points["Latitude"])]

geo_df = gpd.GeoDataFrame(points, crs=crs, geometry=geometry)

map.plot(ax=ax, alpha=0.4, color="grey")
geo_df.plot(ax=ax, markersize=1, color="blue")
plt.show()
