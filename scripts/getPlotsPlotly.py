import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


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



