import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv("data/processed/Clean.csv")
    train = data.sample(frac=0.7, random_state=1337)
    rest = data.drop(train.index)
    validate = rest.sample(frac=0.5, random_state=1337)
    test = rest.drop(validate.index)
    train.to_csv("data/processed/train.csv", index=False)
    validate.to_csv("data/processed/validate.csv", index=False)
    test.to_csv("data/processed/test.csv", index=False)


if __name__ == "__main__":
    main()
