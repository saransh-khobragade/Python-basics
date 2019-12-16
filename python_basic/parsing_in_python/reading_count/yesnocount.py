def main():

	file =open("sample.txt","r")
	lines=file.readlines()
	file.close()
	
	countYes=0
	countNo=0

	for line in lines:
		line=line.strip().upper()
		if line.find("YES")!=-1:
			countYes=countYes+1
		if line.find("NO")!=-1:
			countNo=countNo+1

	print("YES:",countYes)
	print("No:",countNo)

main()