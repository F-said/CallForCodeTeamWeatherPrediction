import pandas as pd
import numpy as np
import math

# Import hurricane data
Hurricane_nyc = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/CallForCodeTeamWeatherPrediction/HurricaneNYCDataSet.csv")

# Drop data columns not relevant to severity in terms of socio-economics
Hurricane_nyc = Hurricane_nyc.drop(labels=["Category_UL", "Humidity_UL(Relative Humidity)", "Total_Duration(estimated_hours)", "Name", "SST_UL(F)", "WindSpeed_UL(mph)"], axis=1)

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
S_se = pd.DataFrame()
S_se["Year"] = list(range(2000, 2018))

freq = freq.reset_index()
# Concatenate date
S_se = pd.concat([S_se, freq], axis=1)

S_se = S_se.drop(labels="index", axis=1)

# Rename frequency column
S_se = S_se.rename(index=str, columns={"Date": "Frequency"})
S_se.to_csv(path_or_buf="S_se.csv", index=False)

# Calculations for S_se done by hand 
'''
# Get distance from average frequency compared to that year
S_se["S_se"] = np.where(S_se["Frequency"] > 0, Hurricane_nyc["Fatalities"]**2 + Hurricane_nyc["Economic_Loss(USD million estimated)"]**2, 0)

S_se.to_csv(path_or_buf="S_se.csv", index=False)
'''
