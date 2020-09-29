import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil

df = pd.read_csv("../data/kepler-data.csv")

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

for col1 in columns:
    if df[col1].dtypes not in ["int64", "float64"] or "id" in col1 or "err" in col1:
        continue
    print(col1)
    for col2 in columns:
        if col1 == col2 or (col1, col2) in covered or (col2, col1) in covered or df[col2].dtypes not in ["int64", "float64"] or "id" in col2 or "err" in col2 or abs(df[col1].corr(df[col2])) < 0.25:
            continue
        correlation = abs(df[col1].corr(df[col2]))
        if correlation > 0.5:
            mode = "high"
        elif 0.3 <= correlation <= 0.5:
            mode = "medium"
        else:
            mode = "low"
        plt.title(f"{col1} vs {col2}")
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.scatter(df[col1].values, df[col2].values, color='lightblue')
        plt.savefig(f"Scatter Plots/{mode}/{col1}-{col2}", dpi=200)
        plt.close("all")
        covered.append((col1, col2))
        covered.append((col2, col1))

covered = []

for col1 in columns:
    if df[col1].dtypes not in ["int64", "float64"] or "id" in col1 or "err" in col1:
        continue
    print(col1)
    for col2 in columns:
        if col1 == col2 or (col1, col2) in covered or (col2, col1) in covered or df[col2].dtypes not in ["int64", "float64"] or "id" in col2 or "err" in col2 or abs(df[col1].corr(df[col2])) < 0.25:
            continue
        correlation = abs(df[col1].corr(df[col2]))
        if correlation > 0.5:
            mode = "high"
        elif 0.3 <= correlation <= 0.5:
            mode = "medium"
        else:
            mode = "low"
        plt.title(f"{col2} vs {col1}")
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.scatter(df[col2].values, df[col1].values, color='lightblue')
        plt.savefig(f"Scatter Plots/{mode}/{col2}-{col1}", dpi=200)
        plt.close("all")
        covered.append((col1, col2))
        covered.append((col2, col1))

for col in columns:
    if df[col].dtypes not in ["int64", "float64"] or "id" in col or "err" in col:
        continue
    print(col)
    plt.hist(df[col].values, color="lightblue")
    plt.title(col)
    plt.savefig(f"Histograms/{col}", dpi=200)
    plt.close("all")


for col in columns:
    if df[col].dtypes in ["int64", "float64"]:
        continue
    data = dict(df[col].value_counts())
    X = list(data.keys())
    y = list(data.values())
    if len(X) > 50:
        continue
    print(col)
    plt.bar(X, y, color="lightblue")
    plt.title(col)
    plt.savefig(rf"Bar Plots/{col}", dpi=200)
    plt.close("all")
