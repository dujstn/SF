import os
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)


#Function to write city names into .txt files from numpy ndarrays


def writeTxt(uniques, name):
    uniquesString = ";".join(uniques)

    txt = open(os.path.join(os.path.dirname(__file__), name), "w")
    txt.write(uniquesString)
    txt.close()

#Function to get a list of unique city names so that they cam be compared


def getUniques(data):
    uniqueCities = pd.Series.unique(data)
    return uniqueCities


# Read data from Insolation & Economics spreadsheets into dataframes
munInso = pd.read_csv(os.path.join(os.path.dirname(__file__), "Municipality Insolation.csv"))
curEcon = pd.read_csv(os.path.join(os.path.dirname(__file__), "Current Economics.csv"))


# Gather unique names of locations inside Economics spreadsheet
curEcon_cities = curEcon.pop('Municipality')
curEcon_uniques = pd.Series.unique(curEcon_cities)
writeTxt(curEcon_uniques, "curEconCities.txt")
curEconCompare = getUniques(curEcon_cities)

# Gather unique names of locations inside Insolation spreadsheet
munInso_cities = munInso.pop('Municipality')
munInso_uniques = pd.Series.unique(munInso_cities)
writeTxt(munInso_uniques, "munInsoCities.txt")
munInsoCompare = getUniques(munInso_cities)

# Find the locations that aren't common to both sets
output = np.setdiff1d(curEconCompare, munInsoCompare)
writeTxt(output, "OutputOne.txt")

# Compared Economics to Insolation; need to do it the other way around
outputTwo = np.setdiff1d(munInsoCompare, curEconCompare)
writeTxt(outputTwo, "OutputTwo.txt")
