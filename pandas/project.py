import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataAnalyzer:

    def __init__(self, file):
        self.file = file
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file)
        print("Dataset Loaded Successfully")

    def information(self):
        print("\nInformation")
        print(self.data.info())

    def statistics(self):
        print("\nStatistics")
        print(self.data.describe())

    def missing_values(self):
        print("\nMissing Values")
        print(self.data.isnull().sum())

    def remove_missing(self):
        self.data = self.data.dropna()
        print("Missing Values Removed")

    def correlation(self):
        print("\nCorrelation Matrix")
        print(self.data.corr(numeric_only=True))

    def top_rows(self):
        print(self.data.head())

    def bottom_rows(self):
        print(self.data.tail())

    def histogram(self, column):
        plt.figure(figsize=(7,5))
        self.data[column].hist(bins=20)
        plt.title(column)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def line_chart(self, x, y):
        plt.figure(figsize=(8,5))
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(y + " vs " + x)
        plt.show()

    def bar_chart(self, x, y):
        plt.figure(figsize=(8,5))
        plt.bar(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(y)
        plt.show()

    def save_clean_data(self, file):
        self.data.to_csv(file, index=False)
        print("File Saved")

analyzer = DataAnalyzer("data.csv")

while True:
    print("\n===== DATA ANALYSIS MENU =====")
    print("1.Load Dataset")
    print("2.Information")
    print("3.Statistics")
    print("4.Top Rows")
    print("5.Bottom Rows")
    print("6.Missing Values")
    print("7.Remove Missing Values")
    print("8.Correlation")
    print("9.Histogram")
    print("10.Line Chart")
    print("11.Bar Chart")
    print("12.Save Clean Data")
    print("13.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        analyzer.load_data()

    elif choice == "2":
        analyzer.information()

    elif choice == "3":
        analyzer.statistics()

    elif choice == "4":
        analyzer.top_rows()

    elif choice == "5":
        analyzer.bottom_rows()

    elif choice == "6":
        analyzer.missing_values()

    elif choice == "7":
        analyzer.remove_missing()

    elif choice == "8":
        analyzer.correlation()

    elif choice == "9":
        column = input("Column Name: ")
        analyzer.histogram(column)

    elif choice == "10":
        x = input("X Column: ")
        y = input("Y Column: ")
        analyzer.line_chart(x, y)

    elif choice == "11":
        x = input("Category Column: ")
        y = input("Value Column: ")
        analyzer.bar_chart(x, y)

    elif choice == "12":
        name = input("Output File Name: ")
        analyzer.save_clean_data(name)

    elif choice == "13":
        break

    else:
        print("Invalid Choice")