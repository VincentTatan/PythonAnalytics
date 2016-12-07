import pandas as pd
# import matplotlib.pyplot as plt

mobile_data = pd.read_excel('MobileData.xlsx', na_values=['NA'])
print(mobile_data.head())
print(mobile_data.describe())

# # Creating data analytics cleaning and combining classes
# iris_data.loc[iris_data['class'] == 'versicolor', 'class'] = 'Iris-versicolor'
# iris_data.loc[iris_data['class'] == 'Iris-setossa', 'class'] = 'Iris-setosa'

# iris_data['class'].unique()

# # This line drops any 'Iris-setosa' rows with a separal width less than 2.5 cm
# iris_data = iris_data.loc[(iris_data['class'] != 'Iris-setosa') | (iris_data['sepal_width_cm'] >= 2.5)]
# iris_data.loc[iris_data['class'] == 'Iris-setosa', 'sepal_width_cm'].hist()	