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


def linear(train: pd.DataFrame, test: pd.DataFrame, target):
    xt = train.drop(columns=target)
    yt = train[target]
    xte = test.drop(columns=target)
    yte = test[target]
    model = LinearRegression()
    model.fit(xt, yt)
    y_pred = model.predict(xte)
    print(f"\nFor target {target}")
    print("MAE :", mean_absolute_error(yte, y_pred))
    print("RMSE:", mean_squared_error(yte, y_pred) ** 0.5)
    print("R2  :", r2_score(yte, y_pred))

def forest_regressors(train: pd.DataFrame, test: pd.DataFrame, target):
    xt = train.drop(columns=target)
    yt = train[target]
    xte = test.drop(columns=target)
    yte = test[target]
    model = RandomForestRegressor(n_estimators=75, max_depth=5, random_state=987)
    model.fit(xt, yt)
    y_pred = model.predict(xte)
    print(f"For target {target}")
    print("MAE :", mean_absolute_error(yte, y_pred))
    print("RMSE:", mean_squared_error(yte, y_pred) ** 0.5)
    print("R2  :", r2_score(yte, y_pred))

def DNN(train: pd.DataFrame, test: pd.DataFrame, val: pd.DataFrame, target):
    xt = train.drop(columns=target)
    yt = train[target]
    xte = test.drop(columns=target)
    yte = test[target]
    xval = val.drop(columns=target)
    yval = val[target]
    model = tf.keras.Sequential([
    layers.Input(shape=(xt.shape[1],)),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(32, activation="relu"),
    layers.Dense(1)                              # regression
    # layers.Dense(1, activation="sigmoid")      # binary classification
    # layers.Dense(n_classes, activation="softmax")  # multi-class
    ])
 
    model.compile(optimizer="adam",
              loss="mse", metrics=["mae"])        # regression
              # loss="binary_crossentropy", metrics=["accuracy"]  # classification
 
    early_stop = tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
    history = model.fit(xt, yt,
                    validation_data=(xval, yval),
                    epochs=200, batch_size=32,
                    callbacks=[early_stop])
    y_pred = model.predict(xte)
    print(f"For target {target}")
    print("MAE :", mean_absolute_error(yte, y_pred))
    print("RMSE:", mean_squared_error(yte, y_pred) ** 0.5)
    print("R2  :", r2_score(yte, y_pred))
    s_target = target.replace("/", "_")
    model.save(f"models/dnn/{s_target}.keras")

def main():
    train = pd.read_csv("data/processed/train.csv")
    test = pd.read_csv("data/processed/test.csv")
    validate = pd.read_csv("data/processed/validate.csv")
    num_train = train.drop(columns=['Station', 'Date', 'outlier score'])
    num_test = test.drop(columns=['Station', 'Date', 'outlier score'])
    num_validate = validate.drop(columns=['Station', 'Date', 'outlier score'])
    cols = num_train.columns.to_list()
    print("SIMPLE LINEAR \n\n\n")
    for col in cols:
        linear(num_train, num_test, col)
    print("\n\n\nRANDOM FOREST\n\n\n")
    for col in cols:
        forest_regressors(num_train, num_test, col)
    print("\n\n\nDNN\n\n\n")
    for col in cols:
        DNN(num_train, num_test, num_validate, col)


if __name__ == "__main__":
    main()