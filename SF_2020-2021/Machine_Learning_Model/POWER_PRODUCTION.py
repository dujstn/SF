import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
np.set_printoptions(threshold=np.inf)

# Data Preparation
train = pd.read_csv("SF_2020-2021/Data/B_TRAIN.csv")
eval = pd.read_csv("SF_2020-2021/Data/B_EVAL.csv")

feats_TRAIN = train[["Latitude", "Longitude", "Array Type", "Total Capacity (MW)", "Annual"]]
trainFeatList = [list(row) for row in feats_TRAIN.values]
label_TRAIN = train[["First Yr Annual (MWh)"]]
trainLabelList = [list(row) for row in label_TRAIN.values]

feats_EVAL = eval[["Latitude", "Longitude", "Array Type", "Total Capacity (MW)", "Annual"]]
evalFeatList = [list(row) for row in feats_EVAL.values]
label_EVAL = eval[["First Yr Annual (MWh)"]]
evalLabelList = [list(row) for row in label_EVAL.values]

model = KNeighborsRegressor()
knn_grid = {'n_neighbors': np.arange(1, 10)}
model_knn = GridSearchCV(model, knn_grid, cv=10)
model_knn.fit(trainFeatList, trainLabelList)
print("Best K Value: ", model_knn.best_params_)
print("R^2 - Training: ", model_knn.best_score_)
output = model_knn.predict(evalFeatList)
print("\n\nAverage Error % (Evaluation, K = 1): ", mean_absolute_error(evalLabelList, output))
print("R^2 - Evaluation: ", model_knn.score(evalFeatList, evalLabelList))

print(output)
