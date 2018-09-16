import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

S_se = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/CallForCodeTeamWeatherPrediction/S_se.csv")

y_axis = S_se[S_se["Frequency"] != 0].drop(labels="Year", axis=1).drop(labels="Frequency", axis=1)
X_axis = S_se[S_se["Frequency"] != 0]["Year"]

# Removed Sandy because of extreme case skewing slope.

# Linear Regression model
X_axis = X_axis.reshape(-1, 1)
reg = linear_model.LinearRegression()
reg.fit(X_axis, y_axis)

X_axis_extended = pd.Series(list(range(2000, 2031)))
X_axis_extended = X_axis_extended.reshape(-1, 1)

y_pred = reg.predict(X_axis_extended)

plt.figure()
plt.scatter(X_axis, y_axis,  color='black')
plt.plot(X_axis_extended, y_pred, color='blue', linewidth=3)

plt.savefig(filename="SseScoreVsYear")
plt.close()

print(reg.coef_)
