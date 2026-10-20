import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow.keras as tk
import pickle


def main():
    test = pd.read_csv("data/processed/test.csv")
    num_test = test.drop(columns=['Station', 'Date', 'outlier score'])
    cols = num_test.columns.to_list()
    accumulate = []
    for col in cols:
        s_target = col.replace("/", "_")
        xte = num_test.drop(columns=col)
        yte = num_test[col]
        with open(f"models/linear/{s_target}.pkl", 'rb') as f:
            linear = pickle.load(f)
        with open(f"models/random_forest/{s_target}.pkl", 'rb') as f:
            forest = pickle.load(f)
        try:
            dnn = tk.models.load_model(f"models/dnn/{s_target}.keras")
        except:
            print(f"model for {col} failed to load")
            continue
        #print(f"\nFor target {col}")
        #print(f"LINEAR")
        y_pred = linear.predict(xte)
        accumulate.append([col, "Linear", mean_absolute_error(yte, y_pred), mean_squared_error(yte, y_pred)**0.5, r2_score(yte, y_pred)])
        ##print(f"FOREST")
        y_pred = forest.predict(xte)
        accumulate.append([col, "Forest", mean_absolute_error(yte, y_pred), mean_squared_error(yte, y_pred)**0.5, r2_score(yte, y_pred)])
        #print(f"DNN")
        y_pred = dnn.predict(xte)
        accumulate.append([col, "DNN", mean_absolute_error(yte, y_pred), mean_squared_error(yte, y_pred)**0.5, r2_score(yte, y_pred)])
    result = pd.DataFrame(accumulate, columns=['Polutant', 'Model', 'Mean Abs Error', 'Mean Squared Error', 'r2 score'])
    result.to_csv("data/processed/stats.csv", index=False)



        
        

if __name__ == "__main__":
    main()