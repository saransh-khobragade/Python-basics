import csv


firstname=input("Enter your name")
lastname=input("Enter your last name")
marks=input("Enter your marks")


f=open("C:\\Users\\Saransh\\Desktop\Python\CsvParsing\\SampleCSV2.csv","a")
csv_writer=csv.writer(f)

csv_writer.writerow([firstname,lastname,marks])


f.close()