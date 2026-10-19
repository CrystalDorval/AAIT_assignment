import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor as lof

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
    plt.clf()
    plt.scatter(data[x], data[y])
    plt.title(f"{y} vs {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(f"plots/{y} vs {x}.png")

def histograms(data):
    check_cols = data.columns.difference(['Station', 'Date'])
    for col in check_cols:
        histogram(data, col)
    return


def histogram(data, x):
    sx = x.replace("/", "_")
    plt.clf()
    counts, bins = np.histogram(data[x], bins=20)
    plt.bar(bins[:-1], counts)
    plt.title(f"{sx} distribution")
    plt.savefig(f"plots/{sx} distribution")

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    station_map = pd.read_csv("data/stations_2026-10-05-180443.csv")
    rename = pd.Series(station_map.Station_Name.values, index=station_map.NAPS_ID)
    data = data.reset_index(drop=True)
    data['Station'] = data['Station'].map(lambda i: rename[i])
    check_cols = data.columns.difference(['Station', 'Date'])
    for col in check_cols:
        data[col] = (data[col]-data[col].min())/(data[col].max()-data[col].min())
    

    return data

def get_outliers(data: pd.DataFrame)-> tuple[pd.DataFrame, pd.DataFrame]:
    detect = lof(n_neighbors=20, contamination=0.05)
    check_cols = data.columns.difference(['Station', 'Date'])
    data["outlier"] = detect.fit_predict(data[check_cols])
    data["outlier score"] = detect.negative_outlier_factor_
    return data[data['outlier'] == 1], data[data['outlier'] == -1]

def main():
    data = load_merged()
    #print(data)
    #get_incomplete_rows(data)
    complete = get_complete(data)
    #print(complete)
    inliers, outliers = get_outliers(complete)
    #inliers.to_csv("data/processed/inliers.csv")
    #outliers.to_csv("data/processed/outliers.csv")
    print(f"detected {len(outliers)} outliers")
    inliers = inliers.drop(columns=['outlier'])
    
    clean = clean_data(inliers)
    clean.to_csv("data/processed/Clean.csv", index=False)
    histograms(clean)
    scatter(clean, "Acetaldehyde", "Benzaldehyde")
    scatter(clean, "Formaldehyde", "Hexanal")


if __name__ == main():
    main()