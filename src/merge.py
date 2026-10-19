import numpy as np
import pandas as pd
import matplotlib as mpl

def clean(data):
    pass

def load_data():
    data = pd.read_csv("data/data_2026-10-05-180443.csv")
    return data

def show_stats(data: pd.DataFrame):
    cols = data.columns.to_list()
    print(f"{cols}")
    streams = data['Monitoring_Stream'].unique()
    for stream in streams:
        d_slice = data[data['Monitoring_Stream']==stream]
        vals = d_slice['Analysis'].unique()
        print(f"In Stream: {stream}")
        print(f"Analsysis has vals: {vals}\n")
        params = d_slice['Parameter'].unique()
        print(f"In Stream: {stream}")
        print(f"Parameter has vals: {params}\n")
    keys = data['Stream_Analysis'].unique()
    for key in keys:
        d_slice = data[data['Stream_Analysis']==key]
        params = d_slice['Parameter'].unique()
        print(f"In Section: {key}")
        print(f"Parameter has vals: {params}\n")

def section_stats(data: pd.DataFrame):
    count = data.shape[0]
    print(f"Selected Section has {count} entries")
    params = data['Parameter'].unique() #grab all parameter values in thee dataa set
    print(f"Params are: {params}")
    stations = data['NAPS_ID'].unique() #grab all stations in the data set
    missing = []
    duplicates = []
    missing_vals = [] #preliminary search shows no duplicates in target area so further analysis on missisng values only
    dates = data['Sampling_Date_yyyy_mm_dd'].unique() #grab all dates that are present in the data set
    sampling_data = data[data['Sample_Type']=='R'] #only account for actual measurements when analyzing duplicates and missing values
    sampling_data = sampling_data[sampling_data['Validation_Code']!='M1']
    sampling_data = sampling_data[sampling_data['Validation_Code']!='M2'] #remove lines that explicitly contain invalid or missing measurements
    for date in dates:
        d_slice = sampling_data[sampling_data['Sampling_Date_yyyy_mm_dd']==date]
        for station in stations:
            s_slice = d_slice[d_slice['NAPS_ID']==station]
            for param in params:
                p_slice = s_slice[s_slice['Parameter']==param]
                l = len(p_slice)
                if l==0:
                    missing.append(f"{param} on {date} missing, in station {station}")
                    missing_vals.append((param, date, station))
                elif l>1:
                    vals = p_slice['Value'].unique()
                    duplicates.append(f"{param} on {date} in station {station} has duplicates with vals {vals}")
    #print(f"Missing: {"\n".join(missing)}")
    #print(f"Duplicates: {"\n".join(duplicates)}")
    print(f"Missing: {len(missing)} entries")
    print(f"With {len(duplicates)} duplicates")
    missing_data = pd.DataFrame(missing_vals, columns=['parameter', 'date', 'station'])
    print(f"{len(missing_data['station'].unique())}/{len(stations)} stations missing data")
    print(f"{len(missing_data['date'].unique())}/{len(dates)} dates missing data")
    print(f"{len(missing_data['parameter'].unique())}/{len(params)} parameters missing data")
    print(f"Missing Dates: {missing_data['date'].unique()}")


def organize(data: pd.DataFrame):
    data["Stream_Analysis"] = data['Monitoring_Stream'] + " " + data['Analysis']

def merge_by_date(data):
    params = data['Parameter'].unique().tolist() #grab all parameter values in thee dataa set
    dates = data['Sampling_Date_yyyy_mm_dd'].unique() #grab all dates that are present in the data set
    stations = data['NAPS_ID'].unique() #grab all stations in the data set
    cols = ['Station', 'Date']+params
    accumulate = []
    for date in dates:
        d_slice = data[data['Sampling_Date_yyyy_mm_dd']==date]
        for station in stations:
            s_slice = d_slice[d_slice['NAPS_ID']==station]
            entry = [station, date]
            for param in params:
                p_slice = s_slice[s_slice['Parameter']==param]
                val = float('NaN')
                if len(p_slice)==1:
                    val = p_slice['Value'].iat[0]
                entry.append(val)
            accumulate.append(entry)
    result = pd.DataFrame(accumulate, columns=cols)
    return result
    




def main():
    data = load_data()
    organize(data)
    #show_stats(data)
    carbonyls = data[data['Monitoring_Stream']=='Carbonyls']
    section_stats(carbonyls)
    nice = merge_by_date(carbonyls)
    print(nice)
    nice.to_csv("data/processed/Merged.csv", index=False)
    cleaned = clean(data)


if __name__ == "__main__":
    main()