d = {'koi_depth': 59,
     'koi_impact': 59,
     'koi_insol': 17,
     'koi_kepmag': 1,
     'koi_model_snr': 59,
     'koi_prad': 59,
     'koi_score': 1206,
     'koi_slogg': 59,
     'koi_srad': 59,
     'koi_steff': 59,
     'koi_tce_delivname': 255,
     'koi_tce_plnt_num': 255,
     'koi_teq': 59}

columns = list(d.keys())

s1 = '''plt.scatter(range(df.shape[0]), df["{}"].values, label = "Depth")
plt.title("Depth")
plt.legend()'''

s2 = '''plt.hist(df["{}"].values, bins=5, color="lightblue")
plt.axvline(x = np.nanpercentile(df["{}"].values, 0), color = "green", label = "0th")
plt.axvline(x = np.nanpercentile(df["{}"].values, 25), color = "blue", label = "25th")
plt.axvline(x = np.nanpercentile(df["{}"].values, 50), color = "yellow", label = "50th")
plt.axvline(x = np.nanpercentile(df["{}"].values, 75), color = "black", label = "75th")
plt.axvline(x = np.nanpercentile(df["{}"].values, 99.6), color = "red", label = "99.6th")
plt.axvline(x = np.nanpercentile(df["{}"].values, 100), color = "purple", label = "100th")
plt.title("Frequency Distribution for Orbital Period Error 1")
plt.legend()
plt.show()'''

s3 = '''df["{}"].fillna(np.nanpercentile(df["{}"].values, 99.6), inplace = True)'''

for col in columns:
    print(s1.format(col))
    print("\n")
    print(s2.format(col, col, col, col, col, col, col))
    print("\n")
    print(s3.format(col, col))
    print("\n")
    print("######################################################################################################################")
