import bs4 as bs 
import urllib
import pandas as pd

# Reading from XML
# sauce = urllib.urlopen('https://www.washingtonpost.com/news-sitemap-index.xml').read()
# soup = bs.BeautifulSoup(sauce,'xml')
# print(soup)
# for url in soup.find_all('loc'):
# 	print(url.text)

# Reading from HTML
# sauce = urllib.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')

# Panda web table parsing
#Collect and combine many data finance
companies = ['GOOG','TSLA']
indexbid = ['Open','Prev Close','Bid','Ask','Day\'s range','52wk range','1y TargetEst']
indexmarket = ['Market Cap','P/E Ratio (ttm)','Beta','Volume','Avg Vol (3m)','Dividend & Yield','Earnings Date']

columns=['Attribute']
aggbiddfs = pd.DataFrame(index=indexbid, columns=columns)
aggmarketdfs = pd.DataFrame(index=indexmarket, columns=columns)
for company in companies:
	dfs= pd.read_html('https://finance.yahoo.com/quote/'+company+'?p='+company, index_col=[0])
	biddf = dfs[1]
	marketdf = dfs[2]
	aggbiddfs.concatenate(biddf)
	aggmarketdfs.concatenate(marketdf)

print aggbiddfs
print aggmarketdfs
