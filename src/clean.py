import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_merged():
    data = pd.read_csv("data/processed/Merged.csv")
    return data


def get_incomplete_rows(data):
    incomp = data[data.isna().any(axis=1)]
    print(incomp)
    check_cols = incomp.columns.difference(['Station', 'Date'])
    partial = incomp[incomp[check_cols].notna().any(axis=1)]
    print(partial) # verify that there are no empty columns, analysis of days and locations with data should be sufficient with oover 1000 rows

def get_complete(data):
    check_cols = data.columns.difference(['Station', 'Date'])
    return data[data[check_cols].notna().all(axis=1)]

def scatter(data, x, y):
    plt.scatter(data[x], data[y])
    plt.title(f"{y} vs {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(f"plots/{y} vs {x}.png")


def main():
    data = load_merged()
    #print(data)
    #get_incomplete_rows(data)
    complete = get_complete(data)
    #print(complete)
    scatter(complete, "Acetaldehyde", "Benzaldehyde")


if __name__ == main():
    main()