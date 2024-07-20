#blank dicktionary
dic={}
dic["a"]=5
dic["b"]=10

#how to loop over dictionary
for x, y in dic.items():
  print(x, y)

for x in dic.keys():
  print(x)

for y in dic.values():
  print(y)

#how to check key exists in dictionary
if 'x' in dic:
    dic['x']+=1
else:
    dic['x']=1


# Set unique but no unordered
set_itmes = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
print(set_itmes)

# Dictionary key value pairs can use immutable keys mutabale values
dictionary = {
    'A': 12,
    'B': 122,
    'C': 45,
    'D': 76,
    'E': 23,
    'F': 2323
}
print(dictionary)

print(dictionary.keys())
print(dictionary.values())


#add item or update to dictionary
dictionary['G'] = 31
dictionary.update({'G': 32})


#loop in dict
for x, y in dictionary.items():
  print(x, y)

#sorting dictionary by its values and converting to list to tuple
print(sorted(dictionary.items(), key=lambda x:x[1] ,reverse=False))

#sorting dictionary by its keys and converting to list to tuple
print(sorted(dictionary.items(), key=lambda x:x[0] ,reverse=False))

#complex key in dictionary using tupple
d = {}
d[("a","b","c")]=1
print(d)



