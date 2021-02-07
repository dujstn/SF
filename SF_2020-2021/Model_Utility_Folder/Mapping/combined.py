import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import descartes
import os
from shapely.geometry import Point

# Defining map characteristics
map = gpd.read_file(
    "SF/SF_2020-2021/Model_Utility_Folder/Mapping/Shapefile/gpr_000b11a_e.shp")
fig, ax = plt.subplots(figsize=(30, 30))
crs = {"init": "epsg:4326"}

# Defining Points and Geometry for usables and unusable Econ + Inso data
usablePoints = pd.read_csv("SF/SF_2020-2021/Data/Usables.csv")
usableGeometry = [Point(xy) for xy in zip(usablePoints["Longitude"], usablePoints["Latitude"])]

unusableEconPoints = pd.read_csv("SF/SF_2020-2021/Data/UnusableEcon.csv")
unusableEconGeometry = [Point(xy) for xy in zip(
    unusableEconPoints["Longitude"], unusableEconPoints["Latitude"])]

unusableInsoPoints = pd.read_csv("SF/SF_2020-2021/Data/UnusableInso.csv")
unusableInsoGeometry = [Point(xy) for xy in zip(unusableInsoPoints["Longitude"], unusableInsoPoints["Latitude"])]

# Changing from dataFrame to geoDataFrame
usableGeo = gpd.GeoDataFrame(usablePoints, crs=crs, geometry=usableGeometry)
unusableEconGeo = gpd.GeoDataFrame(unusableEconPoints, crs=crs, geometry=unusableEconGeometry)
unusableInsoGeo = gpd.GeoDataFrame(unusableInsoPoints, crs=crs, geometry=unusableInsoGeometry)

# Plotting final map
map.plot(ax=ax, alpha=0.4, color="grey")
usableGeo.plot(ax=ax, markersize=5, color="blue")
unusableEconGeo.plot(ax=ax, markersize=5, color="red")
unusableInsoGeo.plot(ax=ax, markersize=5, color="green")
plt.show()
