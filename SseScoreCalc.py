import pandas as pd
import numpy as np

# Import hurricane data
Hurricane_nyc = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/CallForCodeTeamWeatherPrediction/HurricaneNYCDataSet.csv")

# Drop data columns not relevant to severity in terms of socio-economics
Hurricane_nyc = Hurricane_nyc.drop(labels=["Category_UL", "Humidity_UL(Relative Humidity)", "Total_Duration(estimated_hours)", "Name"], axis=1)

# Extract date
Hurricane_nyc["Date"] = Hurricane_nyc["Date"].str.slice(-4)

# Get frequency of date
freq = Hurricane_nyc["Date"].value_counts().sort_index()

# Fill in years without any count with 0
years = list(range(2000, 2018))
for y in years:
    if str(y) not in freq.index:
        freq[str(y)] = 0
freq = pd.DataFrame(freq.sort_index())

# Create dataframe to hold years from 2000-2017
S_h = pd.DataFrame()
S_h["Year"] = list(range(2000, 2018))

freq = freq.reset_index()
# Concatenate date
S_h = pd.concat([S_h, freq], axis=1)

S_h = S_h.drop(labels="index", axis=1)

# Rename frequency column
S_h = S_h.rename(index=str, columns={"Date": "Frequency"})

# Get distance from average frequency compared to that year
S_h["Distance_From_Avg"] = np.where(S_h["Frequency"] > 0, (S_h["Frequency"] - S_h["Frequency"].mean()), 0)

# Get Wind_Speed/SST measure since Wind Speed and SSt are inversely correlated
# Just zero everything out and fill it out yourself its legit only 9 datapoints
S_h["WindSpeed/SST"] = [0] * 18
S_h["Category"] = [0] * 18

S_h.to_csv(path_or_buf="S_h.csv", index=False)

