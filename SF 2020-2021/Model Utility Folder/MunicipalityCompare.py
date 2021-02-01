import os
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)


# Read data from Insolation & Economics spreadsheets into dataframes
munInso = pd.read_csv(os.path.join(os.path.dirname(__file__), "Municipality Insolation.csv"))
curEcon = pd.read_csv(os.path.join(os.path.dirname(__file__), "Current Economics.csv"))

# Gather unique names of locations inside Economics spreadsheet
curEcon_cities = curEcon.pop('Municipality')
curEcon_uniques = pd.Series.unique(curEcon_cities)
curEcon_string = ";".join(curEcon_uniques)
curEconTxt = open(os.path.join(os.path.dirname(__file__), "currentEconomicCities.txt"), "w")
curEconTxt.write(curEcon_string)
curEconTxt.close()

# Gather unique names of locations inside Insolation spreadsheet
munInso_cities = munInso.pop('Municipality')
munInso_uniques = pd.Series.unique(munInso_cities)
munInso_string = ";".join(munInso_uniques)
munInsoTxt = open(os.path.join(os.path.dirname(__file__), "muniInsolationCities.txt"), "w")
munInsoTxt.write(munInso_string)
munInsoTxt.close()

# Find the locations that aren't common to both sets
output = np.setdiff1d(curEcon_uniques, munInso_uniques)
outputString = ";".join(output)
outputTxt = open(os.path.join(os.path.dirname(__file__), "Notcommon.txt"), "w")
outputTxt.write(outputString)
outputTxt.close()

# Compared Economics to Insolation; need to do it the other way around
outputTwo = np.setdiff1d(munInso_uniques, curEcon_uniques)
outputStringTwo = ";".join(outputTwo)
outputTwoTxt = open(os.path.join(os.path.dirname(__file__), "Notcommontwo.txt"), "w")
outputTwoTxt.write(outputStringTwo)
outputTwoTxt.close()
