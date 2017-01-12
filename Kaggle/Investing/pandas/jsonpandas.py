import pandas as pd
import json

f = open('assignment_8.json','rb')

df= pd.DataFrame()

for line in f: 
	linedf = pd.read_json(line,lines=True)
	df=df.append(linedf)

# The existence of multivariate
df['_id'] = [d.get('$oid') for d in df['_id']]
# df["Earnings Date"] = [d.get('$date') for d in df["Earnings Date"]]

# Setting index
df = df.set_index(['_id'])


# Writing it to Excelsheet
writer = pd.ExcelWriter('output.xlsx')
df[['Ticker','Sector','Volatility (Week)',"Price"]].to_excel(writer,'Sheet1')
writer.save()

