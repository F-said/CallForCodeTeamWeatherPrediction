import pandas as pd
import matplotlib.pyplot as plt

hurricanes = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/CallForCodeTeamWeatherPrediction/atlantic.csv")
hurricanes_by_year = hurricanes["Date"]

hurricanes_by_year = hurricanes_by_year.apply(str)
hurricanes_by_year = hurricanes_by_year.str.slice(0, 4)

hurricanes_by_year = hurricanes_by_year.apply(int)

hurricanes_by_year = hurricanes_by_year.value_counts().sort_index()

plt.figure()
hurricanes_by_year.plot()
plt.savefig(filename="HurricanesByYear")
plt.close()
