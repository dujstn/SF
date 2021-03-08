import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import pickle

# CORE MODEL
class knn():
    # Mean calculation
    def mean(self, labels):
        return sum(labels)/len(labels)

    # Euclidean distance for KNN
    def euclidDis(self, ptOne, ptTwo):
        distanceSqrdSum = 0
        for i in range(len(ptOne)):
            distanceSqrdSum += math.pow(ptOne[i] - ptTwo[i], 2)
        return math.sqrt(distanceSqrdSum)

    # Fit data to model
    def fit(self, data, query):
        dictionary = []
        for item in query:
            distAndIndi = []
            for index, example in enumerate(data):
                distance = self.euclidDis(example[:-1], item)
                distAndIndi.append((distance, index))
            dictionary.append(distAndIndi)
        return dictionary

    # Evaluate data and make predictions
    def predict(self, data, query, k, dictionary):
        listPredictedChoice = []
        listPredictedDist = []
        distAndIndi = dictionary

        for item in query:
            distAndIndi_sorted = sorted(distAndIndi)
            distAndIndi_K = distAndIndi_sorted[:k]
            nearestLabels_K = [data[i][-1] for distance, i in distAndIndi_K]

            listPredictedChoice.append(self.mean(nearestLabels_K))
            listPredictedDist = listPredictedDist + distAndIndi_K

        return listPredictedChoice


# Main function
train = pd.read_csv("SF_2020-2021/Data/TRAIN.csv")
eval2 = pd.read_csv("SF_2020-2021/Data/EVAL.csv")

feats_TRAIN = train[["Array Type", "Market Pricing", "Utility-scale Tariff Applied", "First Yr Annual (MWh)", "Reference Price ($/MWh)", "Total Capacity (MW)", "Breakeven Price ($/MWh)"]]
trainList = [list(row) for row in feats_TRAIN.values]

feats_EVAL = eval2[["Array Type", "Market Pricing", "Utility-scale Tariff Applied", "First Yr Annual (MWh)", "Reference Price ($/MWh)", "Total Capacity (MW)"]]
evalList = [list(row) for row in feats_EVAL.values]

# Model fitting

output = knn()
model = output.fit(trainList, evalList)
print(model)


# PICKLE TO SAVE AND LOAD STATES OF MODEL
filename = "SF_2020-2021/Model_Utility_Folder/Validation/pickle.pkl"


with open(filename, "wb") as file:
    pickle.dump(model, file)

"""
with open(filename, "rb") as file:
    model = pickle.load(file)
"""
"""
# Prepping data for evaluation
x = open("SF_2020-2021/Model_Utility_Folder/Validation/distAndIndi.txt").read()
output = [list(value) for value in x.split("; ")]
list = []
for i in output:
    list.append("".join(i))
aux = []
for value in list:
    x = value.split(", ")
    x[0] = float(x[0])
    x[1] = int(x[1])
    aux.append(x)

# Evaluation of datapoints
model = knn()
print(aux)
x = model.predict(trainList, evalList, k=1, dictionary=aux)
"""

# CV
"""
grid = {"k": np.arange(1, 8)}
model = knn(trainList, evalList, k=1, distanceFN=euclidDis, choiceFN=mean)
gcsv = GridSearchCV(model, grid, cv=5)
gcsv.fit(trainList, evalList)

print(gcsv.cv_results_)
print(gcsv.best_params_)
"""
