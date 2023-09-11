"""
Main cli or app entry point


# Note: This script assumes that all columns in data.csv are numeric.
# If there are non-numeric columns, you'd need to handle or exclude them when computing these statistics.
"""

import pandas as pd


def load_data(filename):
    return pd.read_csv(filename)


def display_salary_larger_than_60000(data):
    print("Salary larger than 60000:")
    print(data[data['Salary'] > 60000])
    print("\n")


def display_basic_statistics(data):
    print("Basic Descriptive Statistics:")
    print(data.describe())
    print("\n")


def main():
    data = load_data('data.csv')
    display_basic_statistics(data)
    display_salary_larger_than_60000(data)


if __name__ == "__main__":
    main()
