import xlsxwriter as xl
import os
import pandas as pd

workbook = xl.Workbook(os.path.join(os.path.dirname(__file__), "InsoFiltered.xlsx"))
worksheet = workbook.add_worksheet()

#data = pd.read_csv(os.path.join(os.path.dirname(__file__), "Municpality Insolation.csv"))
#columns = ["Province", "Municipality", "Month", " S WITH 90", "S WITH LAT", "S WITH LAT+15", "S WITH LAT-15", "2 AXIS TRACK", "S WITH 0"]


worksheet.write("A1", "Hello")
workbook.close()
