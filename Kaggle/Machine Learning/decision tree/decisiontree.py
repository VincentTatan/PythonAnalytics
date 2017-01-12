from textblob import TextBlob
import xlrd

#To facilitate the process, I put body at the first column while deleting all the other columns and save it at diff excelsheet. 
#This expedite the xlsx parsing process

sh = xlrd.open_workbook('sentimentalanalysis.xlsx').sheet_by_index(0);

#Input the results into 2 csv at the same folder

#polarity = open("polarity.csv",'w')
#subjectivity = open("subjectivity.csv",'w')

#input to one csv
sentimentalcsv = open("sentimentalcsv.csv",'w')

#This code will include the header as part of calculation. Just copy paste and take it into account
#For 800k data, it will take around 3 mins
try:
	for rownum in range(sh.nrows):
		blob = TextBlob(str(sh.cell(rownum,0).value))
		correctblob = blob.correct();
		sentimentalcsv.write(str(correctblob)+",")
		sentimentalcsv.write(str(correctblob.sentiment.polarity)+",")
		sentimentalcsv.write(str(correctblob.sentiment.subjectivity)+"\n")
finally:
	polarity.close()
	subjectivity.close()
