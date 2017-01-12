from sklearn.datasets import load_diabetes
from sklearn.datasets import load_boston
#Mean squared error indicates a regression model's error in terms of precision(variance) and accuracy(bias)
from sklearn.metrics import mean_squared_error as mse

#Coefficient of determination is a ratio of explained variance to total variance which demonstrates how the model fits the data
from sklearn.metrics import r2_score

# Linear regression (draw a straight line to minimize the residual sum of squares between observations and predictions)
from sklearn.linear_model import LinearRegression

diabetes= load_diabetes
boston = load_boston

model = LinearRegression()
model.fit(diabetes.data,diabetes.target) 

expected = diabetes.target
predicted = model.predict(diabetes.data)

print ("Linear regression model for diabetes dataset")
print("Mean squared error = %0.3f" % mse(expected,predicted))
print("R2 score = %0.3f" % r2_score(expected,predicted))

# Regularization methods penalize the complexity of a model to limit overfitting and help generalization
# The slope will be more stable and the variance smaller

from sklearn.linear_model import Ridge
model = Ridge(alpha=0.1)
model.fit(diabetes.data,diabetes.target) 

expected = diabetes.target
predicted = model.predict(diabetes.data)

print ("Linear regression model for diabetes dataset")
print("Mean squared error = %0.3f" % mse(expected,predicted))
print("R2 score = %0.3f" % r2_score(expected,predicted))

# Random forest is a method that creates a number of decision tree using the CART algorithm. The general approach is the bootstrap aggregation of the decision tree/ bagging

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(diabetes.data,diabetes.target) 

expected = diabetes.target
predicted = model.predict(diabetes.data)

print ("Linear regression model for diabetes dataset")
print("Mean squared error = %0.3f" % mse(expected,predicted))
print("R2 score = %0.3f" % r2_score(expected,predicted))
