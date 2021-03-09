import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
import pickle
np.set_printoptions(threshold=np.inf)

# Main function
train = pd.read_csv("SF_2020-2021/Data/TRAIN.csv")
eval = pd.read_csv("SF_2020-2021/Data/EVAL.csv")

feats_TRAIN = train[["Array Type", "Market Pricing", "Utility-scale Tariff Applied", "First Yr Annual (MWh)", "Reference Price ($/MWh)", "Total Capacity (MW)"]]
trainFeatList = [list(row) for row in feats_TRAIN.values]
label_TRAIN = train[["Breakeven Price ($/MWh)"]]
trainLabelList = [list(row) for row in label_TRAIN.values]

feats_EVAL = eval[["Array Type", "Market Pricing", "Utility-scale Tariff Applied", "First Yr Annual (MWh)", "Reference Price ($/MWh)", "Total Capacity (MW)"]]
evalFeatList = [list(row) for row in feats_EVAL.values]
label_EVAL = eval[["Breakeven Price ($/MWh)"]]
evalLabelList = [list(row) for row in label_EVAL.values]
evalLabelList = np.array(evalLabelList)

# Evaluation of datapoints
model = KNeighborsRegressor()
knn_grid = {'n_neighbors': np.arange(1, 10)}
model_knn = GridSearchCV(model, knn_grid, cv=10)
model_knn.fit(trainFeatList, trainLabelList)
print("Best K Value: ", model_knn.best_params_)
print("R^2 - Training: ", model_knn.best_score_)
output = model_knn.predict(evalFeatList)
print("\n\nAverage Error % (Evaluation, K = 1): ", mean_absolute_error(evalLabelList, output))
print("R^2 - Evaluation: ", model_knn.score(evalFeatList, evalLabelList))
