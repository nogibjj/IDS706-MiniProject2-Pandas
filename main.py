"""
Main cli or app entry point


# Note: This script assumes that all columns in data.csv are numeric.
# If there are non-numeric columns, you'd need to handle or exclude them when computing these statistics.
"""

import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)


def display_data(data):
    print("Data preview:")
    print(data.head())
    print("\n")


def display_basic_statistics(data):
    print("Basic Descriptive Statistics:")
    print(data.describe())
    print("\n")


def display_median(data):
    print("Median of the columns:")
    for column in data.columns:
        print(f"Median of {column}: {data[column].median()}")
    print("\n")


def display_mode(data):
    print("Mode of the columns:")
    for column in data.columns:
        mode_value = data[column].mode()[0]
        print(f"Mode of {column}: {mode_value}")
    print("\n")


def main():
    data = load_data('data.csv')

    display_data(data)
    display_basic_statistics(data)
    display_median(data)

if __name__ == "__main__":
    main()
