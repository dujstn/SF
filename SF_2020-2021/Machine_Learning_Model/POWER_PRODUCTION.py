import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math

# CORE MODEL
def knn(data, query, k, distanceFN, choiceFN):
    listPredictedChoice = []
    listPredictedDist = []
    for item in query:
        distAndIndi = []

        for index, example in enumerate(data):
            distance = distanceFN(example[:-1], item)

            distAndIndi.append((distance, index))

        distAndIndi_sorted = sorted(distAndIndi)
        distAndIndi_K = distAndIndi_sorted[:k]
        nearestLabels_K = [data[i][-1] for distance, i in distAndIndi_K]

        listPredictedChoice.append(choiceFN(nearestLabels_K))
        listPredictedDist = listPredictedDist + distAndIndi_K

    return listPredictedChoice

# Mean calculation
def mean(labels):
    return sum(labels)/len(labels)

# Euclidean distance for KNN
def euclidDis(ptOne, ptTwo):
    distanceSqrdSum = 0

    for i in range(len(ptOne)):
        distanceSqrdSum += math.pow(ptOne[i] - ptTwo[i], 2)
    return math.sqrt(distanceSqrdSum)

# Main function
train = pd.read_csv("SF_2020-2021/Data/B_TRAIN.csv")
eval2 = pd.read_csv("SF_2020-2021/Data/B_EVAL.csv")

feats_TRAIN = train[["Latitude", "Longitude", "Array Type", "Total Capacity (MW)", "Annual", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "First Yr Annual (MWh)"]]
trainList = [list(row) for row in feats_TRAIN.values]

feats_EVAL = eval2[["Latitude", "Longitude", "Array Type", "Total Capacity (MW)", "Annual", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]]
evalList = [list(row) for row in feats_EVAL.values]

expected = eval2[["First Yr Annual (MWh)"]]
expectedList = [list(row) for row in expected.values]

output = knn(trainList, evalList, k=5, distanceFN=euclidDis, choiceFN=mean)

print(output)
