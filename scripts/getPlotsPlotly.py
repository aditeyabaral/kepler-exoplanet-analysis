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

shutil.rmtree(r"labelled", ignore_errors=True)
shutil.rmtree(r"unlabelled", ignore_errors=True)

os.makedirs(r"labelled/scatter/low")
os.makedirs(r"labelled/scatter/medium")
os.makedirs(r"labelled/scatter/high")
os.mkdir(r"labelled/histogram")

os.makedirs(r"unlabelled/scatter/low")
os.makedirs(r"unlabelled/scatter/medium")
os.makedirs(r"unlabelled/scatter/high")
os.mkdir(r"unlabelled/histogram")

# Produce scatter

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
            fig.write_image(f"unlabelled/scatter/{mode}/{col1}-{col2}.jpeg", scale=5)

            fig = px.scatter(df, x=col1, y=col2, title=f"{col2} vs {col1}", color="koi_disposition")
            fig.write_image(f"labelled/scatter/{mode}/{col1}-{col2}.jpeg", scale=5)
            covered.append((col1, col2))
            covered.append((col2, col1))
        except TypeError:
            continue


# Produce histogram and bar plots with frequency

for col in columns:
    if "id" in col or "err" in col or "name" in col:
        continue
    try:
        print(col)
        fig = px.histogram(df, x=col, title=f"Frequency Distribution of {col}")
        fig.write_image(f"unlabelled/histogram/{col}.jpeg", scale=5)

        fig = px.histogram(df, x=col, title=f"Frequency Distribution of {col}", color="koi_disposition")
        fig.write_image(f"labelled/histogram/{col}.jpeg", scale=5)

        fig = px.pie(df, values='koi_score', names='koi_disposition', title='  something here  ')

    except:
        continue
