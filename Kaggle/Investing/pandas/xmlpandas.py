import bs4 as bs 
import urllib
import pandas as pd

# Reading from XML
sauce = open('assignment_8.xml','rb').read()
soup = bs.BeautifulSoup(sauce,'xml')

# Initialize dataframe
df = pd.DataFrame()

# Iterate the elements inside xml
for dataset in soup.find_all('dataset'):
    localname = dataset.metaInformation.processInformation.referenceFunction.get('name')
    exchangelist=[]
    meanvaluelist=[]
    for exchange in dataset.flowData.find_all('exchange'):
        exchangename = exchange.get("name")
        meanvalue = exchange.get("meanValue") 
        exchangelist.append(exchangename)
        meanvaluelist.append(meanvalue)
    s = pd.Series(meanvaluelist, index=exchangelist)    
    df[localname] = s

df = df.drop_duplicates( keep='last')

# Writing it to Excelsheet
writer = pd.ExcelWriter('outputxml.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()