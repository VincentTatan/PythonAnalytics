import pandas as pd 

# df = pd.read_csv("ZILL-Z77036_MLP.csv")

# df.set_index("Date",inplace = True)

# df.to_csv('newcsv.csv')

# df = pd.read_csv('newcsv.csv',index_col=0)
# print(df.head())

# df.columns=['Austin_HPI']
# print(df.head())

# df.to_csv('newcsv3.csv')
# df.to_csv('newcsv4.csv',header=False)
df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'],index_col=0)
print(df.head())

df.to_html('example.html')

df.rename(columns={'Austin_HPI':'77006_HPI'},inplace=True)
print(df.head())