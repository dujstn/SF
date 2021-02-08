import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math
#import sklearn

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

        #print(type(choiceFN(nearestLabels_K)))

        listPredictedChoice.append(choiceFN(nearestLabels_K))
        listPredictedDist = listPredictedDist + distAndIndi_K


    #return distAndIndi_K, choiceFN(nearestLabels_K)
    #return listPredictedChoice, listPredictedDist
    #print(listPredictedChoice)
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
#def main():

train = pd.read_csv("SF/SF_2020-2021/Data/SOUTHCAN_TRAIN.csv")
eval2 = pd.read_csv("SF/SF_2020-2021/Data/SOUTHCAN_EVAL.csv")

feats_TRAIN = train[["Latitude", "Longitude", "Breakeven Price ($/MWh)", "Reference Price ($/MWh)", "Array Type", "First Yr Annual (MWh)"]]
trainList = [list(row) for row in feats_TRAIN.values]

feats_EVAL = eval2[["Latitude", "Longitude", "Breakeven Price ($/MWh)", "Reference Price ($/MWh)", "Array Type"]]
evalList = [list(row) for row in feats_EVAL.values]

expected = eval2[["First Yr Annual (MWh)"]]
expectedList = [list(row) for row in expected.values]

#input = [46.81, -64.06, 124.1, 145.7, 2.0]
#252.14

#input = [51.29, -114.01, 53.55, 25.98, 5.0]
#84298.5
inputLists=[[46.81, -64.06, 124.1, 145.7, 2.0], [51.29, -114.01, 53.55, 25.98, 5.0]]
#x = sklearn.metrics.accuracy_score


#inputKNN, inputPred = knn(trainList, input, k=25, distanceFN=euclidDis, choiceFN=mean)
output = knn(trainList, evalList, k=1, distanceFN=euclidDis, choiceFN=mean)

suggestedList=[252.14, 84298.5]
#Initialize Main function
#if __name__ == "__main__":
    #main()

print(output)
#listOfAccuracies=[]
#for i in range(len(output)):
    #listOfAccuracies.append((output[i]-suggestedList[i])*100/suggestedList[i])

#from statistics import mean
#print(mean(listOfAccuracies))
