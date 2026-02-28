import numpy as np
from pandas import Series


def task131():
    i = np.arange(8).reshape(8, 1)
    j = np.arange(8)
    matrix = (i + j) % 2

    print(matrix)

def task132():
    array = np.array([np.arange(5) for _ in range(5)])
    print(array)

def task133():
    array = np.random.randint(0, 11, (3, 3, 3))

    print(array)

def task134():
    matrix = np.zeros((5, 5), dtype=int)

    matrix[0, :] = 1
    matrix[-1, :] = 1
    matrix[:, 0] = 1
    matrix[:, -1] = 1

    print(matrix)

def task135():
    array = np.array([1, 2, 4, 1, 5, 7, 8, 1, 12, 64, 11, 5, 1, 8, 7, 9, 0])
    array = np.sort(array)[::-1]
    print(array)

def task136():
    matrix = np.matrix([[1, 4, 21, 4], [5, 78, 7, 8], [9, 11, 1, 12]])
    print("matrix shape: ", matrix.shape)
    print("matrix size: ", matrix.size)
    print("matrix dimensions: ", matrix.ndim)

import pandas as pd

def task231():
    a = Series([1, 2, 3])
    b = Series([4, 12, 1])
    distance = 0
    for i in range(a.size):
        distance += (a[i] - b[i])**2
    print(distance)

def task232():
    data_frame = pd.read_csv("https://raw.githubusercontent.com/akmand/datasets/refs/heads/main/sample_grades.csv")
    print(data_frame.to_string())
    return data_frame

def task233():
    df = task232()
    print("\n\n===================info about data frame===================")
    print(df.head())
    print(df.tail())
    print(df.shape)
    print(df.describe())
    print(df.iloc[1:4])
    newdf = df[df["Project Phase 1"] <= 18]
    print("new data frame:\n", newdf.to_string())

import sklearn as sk

def task332():
    dataFrame = pd.read_csv("https://raw.githubusercontent.com/akmand/datasets/master/iris.csv")
    xmax = dataFrame["sepal_length_cm"].max()
    xmin = dataFrame["sepal_length_cm"].min()

    dataFrame["sepal_length_cm"] = (dataFrame["sepal_length_cm"] - xmin) / (xmax - xmin)

    dataFrame['sepal_width_cm'] = sk.preprocessing.StandardScaler().fit_transform(
        dataFrame[['sepal_width_cm']]
    )

    print("\n\n\nNormalized data:\n\n")
    print(dataFrame.to_string())

task332()