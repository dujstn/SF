import pandas as pd
import os
from statistics import mean
import numpy
from sklearn.metrics import accuracy_score
import csv

file = open("SF_2020-2021/Model_Utility_Folder/Analysis/OutputTxts/B_K2.txt").read()
z = [list(value) for value in file.split(", ")]
output = []
for i in z:
    output.append("".join(i))
predict = [float(i) for i in output]

evaluate = pd.read_csv("SF_2020-2021/Data/B_EVAL.csv")
expected = evaluate[["First Yr Annual (MWh)"]]
expectedList = [list(row) for row in expected.values]
x = []
for i in expectedList:
    i = str(i)[1:-1]
    x.append(i)
actuals = [float(i) for i in x]


listOfAccuracies=[]
for i in range(len(output)):
    listOfAccuracies.append(abs((predict[i]-actuals[i])/actuals[i]*100))

df = pd.DataFrame(data={"Prediction": predict, "Actual": actuals, "Error %": listOfAccuracies})
df.to_csv(os.path.join("SF_2020-2021/Model_Utility_Folder/Analysis", "B_K2.csv"), sep=",", index=False)

def mean(list):
    return sum(list)/len(list)

average = mean(listOfAccuracies)
print(average)
