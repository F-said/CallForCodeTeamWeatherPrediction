import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

S_h = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/CallForCodeTeamWeatherPrediction/S_h.csv")

y_axis = S_h[S_h["Frequency"] != 0].drop(labels="Year", axis=1).drop(labels="Frequency", axis=1).sum(axis=1)
X_axis = S_h[S_h["Frequency"] != 0]["Year"]

# Linear Regression model
X_axis = X_axis.reshape(-1, 1)
reg = linear_model.LinearRegression()
reg.fit(X_axis, y_axis)

y_pred = reg.predict(X_axis)

plt.figure()
plt.scatter(X_axis, y_axis,  color='black')
plt.plot(X_axis, y_pred, color='blue', linewidth=3)

plt.savefig(filename="ShScoreVsYear")
plt.close()

print(reg.coef_)
