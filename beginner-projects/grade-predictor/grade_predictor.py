from sklearn.linear_model import LinearRegression
import numpy as np

#training data
hours = [1, 2, 3, 4, 5, 6, 7, 8]
grades = [50, 55, 65, 70, 80, 90, 95, 100]
## hours is the input data, grades is the output data


#turn Lists into arrays for skLearn
X = np.array(hours).reshape(-1, 1)
Y = np.array(grades)

#create and train model
model = LinearRegression()
model.fit(X, Y)
## model.fit(X, Y) learns the pattern between study hours and grades


print("Predicted grade for 0 study hours: {:.2f}".format(model.predict([[0]])[0]))
print("Predicted grade for 3 study hours: {:.2f}".format(model.predict([[3]])[0]))
print("Predicted grade for 7 study hours: {:.2f}".format(model.predict([[7]])[0]))
print("Predicted grade for 8 study hours: {:.2f}".format(model.predict([[8]])[0]))
## Prints based on the pattern learned what grade is expected 
## {: .2f} formats the output to 2 decimal places


import matplotlib.pyplot as plt

# scatter plot(actual data)
plt.scatter(hours, grades, color='blue', label="Actual Data")

# regression Line (model prediction)
plt.plot(hours, model.predict(X), color='red', label="Model Prediction")

plt.xlabel("Hours Studied")
plt.ylabel("Grade")
plt.title("Study Hours vs Grade Prediction")

plt.legend()
plt.show()