
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer

def predictor(tasks):
    taskString = ""
    print(tasks)
    df = pd.read_csv("train.csv")
    X = df["Task"]
    y = df["Stress"]
    print(X.shape)
    print(y)

    for t in tasks: 
        taskString = taskString + " " + t
    print(taskString)
    print("after task string")


    pipe = make_pipeline(CountVectorizer(), SVC())
    print("before fit")
    print(X.to_frame())
    print(y.to_frame())
    pipe.fit(X, y)
    print("before predictX")
    predictX = pd.DataFrame({'Task': tasks}) 
    print("predictX")
    print(predictX)
    predictedStress = pipe.predict(predictX)
    print(predictedStress)
    return predictedStress
