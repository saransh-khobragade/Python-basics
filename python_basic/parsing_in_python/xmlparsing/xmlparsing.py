import xml.dom.minidom

document=xml.dom.minidom.parse("C:\\Users\\Saransh\\Desktop\\Python\\xmlparsing\\xml.xml")


titles=document.getElementsByTagName("title")
for t in titles:
   text=t.firstChild
   title=text.data
   print(title)
   

   
        