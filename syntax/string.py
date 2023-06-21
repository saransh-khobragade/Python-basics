#LENGTH OF STRING----------------------------------------
a = "Hello, World!"
print(len(a)) #13

#CHECK IN STRING----------------------------------------
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "abc" not in txt:
  print("Yes, 'abc' not is present.")


#SLICE----------------------------------------------------
#Saransh
#0123456

str = "Saransh"
print(str[1])   #a from index 1 only one element
print(str[-2])  #s from last second index only one element
print(str[2:5]) #llo [including:excluding]


#sorted()----------------------------------------------------
print(sorted("abc")) #['a', 'b', 'c']

