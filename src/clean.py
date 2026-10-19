import numpy as np
import pandas as pd
import matplotlib as mpl

def load_merged():
    data = pd.read_csv("data/processed/Merged.csv")
    return data



def main():
    data = load_merged()
    print(data)

if __name__ == main():
    main()