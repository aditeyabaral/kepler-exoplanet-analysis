# -*- coding: utf-8 -*-
"""Plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ASvKR2WVfhfRICKS2agCrTunSwPcTbLO
"""

import plotly.express as px
import pandas as pd
df = pd.read_csv("[CLEANED]kepler-data.csv")
df["koi_disposition"].replace({"CANDIDATE":"FALSE POSITIVE"}, inplace=True)
print(df.shape)
df.head()

fig = px.scatter(df, x="koi_insol", y="koi_teq", color="koi_disposition")
fig.show()

fig = px.scatter_3d(df, x='koi_srad', y='koi_prad', z='koi_slogg', color='koi_disposition')
fig.show()

fig = px.pie(df, values='koi_score', names='koi_disposition', title='  something here  ')
fig.show()

fig = px.pie(df, values='koi_score', names='koi_pdisposition', title='  something here  ')
fig.show()

fig = px.histogram(df, x="koi_pdisposition", color="koi_disposition")
fig.show()

fig = px.histogram(df, x="koi_disposition")
fig.show()

fig = px.histogram(df, x="koi_period")
fig.show()



fig = px.histogram(df, x="koi_duration", color="koi_disposition")
fig.show()

fig = px.histogram(df, x="koi_teq", color="koi_disposition")
fig.show()

fig = px.histogram(df, x="koi_steff", color="koi_disposition")
fig.show()

fig = px.histogram(df, x="koi_slogg", color="koi_disposition")
fig.show()

fig = px.histogram(df, x="ra", color="koi_disposition")
fig.show()

