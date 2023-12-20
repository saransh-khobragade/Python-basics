text_file=open("C:\\Users\\Saransh\\Desktop\\Python\\textFilecreationtest.txt","w")
text_file.write("Line 1\n")
text_file.write("Line 2\n")
text_file.write("Line 3\n")

lines=["line1","line2","line3"]
text_file.writelines(lines)

text_file.close()