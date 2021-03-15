import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

# Data Preparation
train = pd.read_csv("SF_2020-2021/Data/TRAIN.csv")
eval = pd.read_csv("SF_2020-2021/Data/EVAL.csv")

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
print(model_knn.cv_results_)

p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = model_knn.cv_results_["split0_test_score"]
one = model_knn.cv_results_["split1_test_score"]
two = model_knn.cv_results_["split2_test_score"]
three = model_knn.cv_results_["split3_test_score"]
four = model_knn.cv_results_["split4_test_score"]
five = model_knn.cv_results_["split5_test_score"]
six = model_knn.cv_results_["split6_test_score"]
seven = model_knn.cv_results_["split7_test_score"]
eight = model_knn.cv_results_["split8_test_score"]
nine = model_knn.cv_results_["split9_test_score"]
splits = [zero, one, two, three, four, five, six, seven, eight, nine]

for i in range(len(splits)):
    plt.plot(p, splits[i], '-o', label= "Number of Splits: " + str(i))

plt.xlabel("K Value", fontsize=30)
plt.ylabel("R-Squared Value", fontsize=30)
plt.title("R-Squared Values - Power Production (Various Splits)", fontsize = 30)
plt.legend()
plt.show()
