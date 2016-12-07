import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing excelsheet of data
df = pd.read_excel('adsense.xlsx', 'adsense', index_col=None, na_values=['NA'])
# df = pd.read_csv('foo.csv')

# Print the head and values of the data
# ---------------------------------------------------
# print(df.head())
# print(df.values)
# Describe the data frame
# print(df.describe())
# Sorting values
# print(df.sort_values(by='Polarity',ascending=False))

# Getting the value
# ---------------------------------------------------
# print(df['Subjectivity'])
# print(df.loc[:,['Subjectivity','Polarity']])
# print(df[df.Polarity>0])


# Transformation data
# ---------------------------------------------------
# df1.dropna(how='any')
# df1.fillna(value=5)
# print(df.mean())
# print(df.mean(1))
# print(df['Subjectivity'].apply(np.cumsum))
# print(df['Subjectivity'].apply(lambda x: x.max() - x.min()))



# Merging data
# ---------------------------------------------------
# pieces = [df[:3], df[3:7], df[7:]]
# pd.concat(pieces)
# pd.merge(left, right, on='key')
# df.append(s, ignore_index=True)

# print(df.groupby(['dominant topic']).sum())

# Time Series
# print(df.groupby(['date']).sum())


# Categories

# Plotting
ts = pd.Series(np.random.randn(2994),index=df["date"])
print(ts)
print(ts.plot())


