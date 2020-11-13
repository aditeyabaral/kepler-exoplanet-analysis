import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/[CLEANED]kepler-data.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)
columns = df.columns
covered = []

shutil.rmtree(r"Scatter Plots", ignore_errors=True)
shutil.rmtree(r"Histograms", ignore_errors=True)
shutil.rmtree(r"Bar Plots", ignore_errors=True)
os.makedirs(r"Scatter Plots/low")
os.makedirs(r"Scatter Plots/medium")
os.makedirs(r"Scatter Plots/high")
os.mkdir(r"Histograms")
os.mkdir(r"Bar Plots")

# Produce Scatter Plots

for col1 in columns:
    if "id" in col1 or "err" in col1: # Skip errors and IDs
        continue
    print(col1)
    for col2 in columns:
        if col1 == col2 or (col1, col2) in covered or (col2, col1) in covered or "id" in col2 or "err" in col2: # Skip redundant, errors, IDs
            continue
        try:
            correlation = abs(df[col1].corr(df[col2])) # Identify the type of correlation - low, medium, high
            if correlation > 0.5:
                mode = "high"
            elif 0.3 <= correlation <= 0.5:
                mode = "medium"
            else:
                mode = "low"
            plt.title(f"{col2} vs {col1}")
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.scatter(df[col1].values, df[col2].values, color='lightblue')
            plt.savefig(f"Scatter Plots/{mode}/{col1}-{col2}", dpi=200)
            plt.close("all")
            covered.append((col1, col2))
            covered.append((col2, col1))
        except:
            continue


# Produce histograms

for col in columns:
    if "id" in col or "err" in col:
        continue
    try:
        print(col)
        plt.hist(df[col].values, color="lightblue")
        plt.title(col)
        plt.savefig(f"Histograms/{col}", dpi=200)
        plt.close("all")
    except:
        continue


# Produce Bar Plots

for col in columns:
    if df[col].dtypes in ["int64", "float64"]:
        continue
    data = dict(df[col].value_counts())
    X = list(data.keys())
    y = list(data.values())
    if len(X) > 50: # More than 50 unique values --> no point in plotting
        continue
    print(col)
    plt.bar(X, y, color="lightblue")
    plt.title(col)
    plt.savefig(rf"Bar Plots/{col}", dpi=200)
    plt.close("all")
