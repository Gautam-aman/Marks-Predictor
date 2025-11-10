
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")


data = pd.read_csv("Study Hours vs Marks.csv")

X = data[['Study_Hours_Per_Week']]
y  = data['Marks_Scored']

model = LinearRegression()
model.fit(X, y)

predicted_score = model.predict(X)


mae = mean_absolute_error(predicted_score , y)
mse = mean_squared_error(predicted_score , y)
rmse = np.sqrt(mse)
r2 = r2_score(predicted_score , y)
print("MSE: ", round(mse,2))
print("RMSE: ", round(rmse,2))
print("MAE: ", round(mae,2))
print("R2 Score: ", round(r2,2)) #closer to 1 == better

#histogram

plt.figure(figsize=(10, 6))
plt.hist(predicted_score , bins=50 , color='blue' , edgecolor='black')
plt.title('Histogram of Predicted Score')
plt.xlabel("Final Score")
plt.ylabel("Study Hours Per Week")
plt.grid(True)
plt.show()


#scatter + prediction

plt.figure(figsize=(10, 6))
plt.scatter(predicted_score , y , color='blue' , edgecolor='black')
plt.plot(predicted_score , y , color='red' , linestyle='--')
plt.xlabel("Final Score")
plt.ylabel("Study Hours Per Week")
plt.grid(True)
plt.show()

value = int(input("Enter your study hours: "))
ans = model.predict([[value]])
print(f"Predicted Marks: {ans[0]:.2f}")










