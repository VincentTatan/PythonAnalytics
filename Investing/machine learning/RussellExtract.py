tickers= []

def parseRus():
	try:
		readFile = open('Russell3000.txt','r').read()
		splitFile = readFile.split('\n')
		for eachLine in splitFile:
			if eachLine:
				tickers.append(eachLine.split(' ')[-1])
		return tickers
	except Exception,e:
		print str(e)
		
