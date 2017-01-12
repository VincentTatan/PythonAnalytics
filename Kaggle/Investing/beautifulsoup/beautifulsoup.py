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
sauce = urllib.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup.title.string)
# print(soup.title.text)
# print(soup.p)
# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
# 	print(paragraph.text.encode('utf-8'))

# print(soup.get_text().encode('utf-8'))

# for url in soup.find_all('a'):
# 	print(url.get('href'))
# Navigating around website
# nav= soup.nav
# for url in nav.find_all('a'):
# 	print(url.get('href'))

# body = soup.body
# for paragraph in body.find_all('p'):
# 	print(paragraph.text.encode('utf-8'))

# for div in soup.find_all('div',class_='body'):
# 	print(div.text.encode('utf-8'))

# Table
# table = soup.table
# table_rows = table.find_all('tr')
# for tr in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text.encode('utf-8') for i in td]
# 	print row

# Panda web table parsing
# dfs= pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
# for df in dfs:
# 	print(df)

print('Hello',4+2)