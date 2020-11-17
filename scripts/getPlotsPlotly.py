import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# $ conda install -c plotly plotly-orca

df = pd.read_csv("../data/[CLEANED]kepler-data.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)
columns = df.columns
covered = []

shutil.rmtree(r"Labelled", ignore_errors=True)
shutil.rmtree(r"Unlabelled", ignore_errors=True)

os.makedirs(r"Labelled/Scatter Plots/low")
os.makedirs(r"Labelled/Scatter Plots/medium")
os.makedirs(r"Labelled/Scatter Plots/high")
os.mkdir(r"Labelled/Histograms")

os.makedirs(r"Unlabelled/Scatter Plots/low")
os.makedirs(r"Unlabelled/Scatter Plots/medium")
os.makedirs(r"Unlabelled/Scatter Plots/high")
os.mkdir(r"Unlabelled/Histograms")

# Produce Scatter Plots

for col1 in columns:
    if "id" in col1 or "err" in col1 or "name" in col1 or "flag" in col1 or "num" in col1:  # Skip errors and IDs
        continue
    print(col1)
    for col2 in columns:
        if col1 == col2 or (col1, col2) in covered or (col2, col1) in covered or "id" in col2 or "err" in col2 or "name" in col2 or "flag" in col2 or "num" in col2:  # Skip redundant, errors, IDs
            continue
        try:
            # Identify the type of correlation - low, medium, high
            correlation = abs(df[col1].corr(df[col2]))
            if correlation > 0.5:
                mode = "high"
            elif 0.3 <= correlation <= 0.5:
                mode = "medium"
            else:
                mode = "low"
            fig = px.scatter(df, x=col1, y=col2, title=f"{col2} vs {col1}")
            fig.write_image(f"Unlabelled/Scatter Plots/{mode}/{col1}-{col2}.jpeg")

            fig = px.scatter(df, x=col1, y=col2, title=f"{col2} vs {col1}", color="koi_disposition")
            fig.write_image(f"Labelled/Scatter Plots/{mode}/{col1}-{col2}.jpeg")
            covered.append((col1, col2))
            covered.append((col2, col1))
        except TypeError:
            continue


# Produce histograms

for col in columns:
    if "id" in col or "err" in col or "name" in col:
        continue
    try:
        print(col)
        fig = px.histogram(df, x=col, title=f"Frequency Distribution of {col}")
        fig.write_image(f"Unlabelled/Histograms/{col}.jpeg")

        fig = px.histogram(df, x=col, title=f"Frequency Distribution of {col}", color="koi_disposition")
        fig.write_image(f"Labelled/Histograms/{col}.jpeg")
    except:
        continue
