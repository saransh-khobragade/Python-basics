import csv
f=open("C:\\Users\\Saransh\\Desktop\Python\CsvParsing\\SampleCSV.csv")
csv_f=csv.reader(f)

for row in csv_f:
    print(row[0]) 


f.close()