import pandas as pd
import os

x = os.path.join("SF/SF 2020-2021/Model Utility Folder/Filtering", "FilteredInso.csv")

print(x)

y = pd.read_csv(x)

print(y.head())
