arr = ["apple", "banana", "cherry","berry","carry"]

print(arr[0])   #apple

#Length
print(len(arr)) #5

#Add item
arr.append("pineapple")
print(arr) #['apple', 'banana', 'cherry', 'berry', 'carry', 'pineapple']

#Insert at index
arr.insert(2,"potatoe")
print(arr)  #['apple', 'banana', 'potatoe', 'cherry', 'berry', 'carry', 'pineapple']

#Extend/merge
arr2 = ("kiwi", "orange")
arr.extend(arr2)
print(arr) #['apple', 'banana', 'potatoe', 'cherry', 'berry', 'carry', 'pineapple', 'kiwi', 'orange']

#Remove
arr.remove("apple")
print(arr)  #['banana', 'potatoe', 'cherry', 'berry', 'carry', 'pineapple', 'kiwi', 'orange']

#Remove at index
arr.pop(0)
print(arr)  #['potatoe', 'cherry', 'berry', 'carry', 'pineapple', 'kiwi', 'orange']

#Sort list
arr.sort()
print(arr) #['berry', 'carry', 'cherry', 'kiwi', 'orange', 'pineapple', 'potatoe']
arr.sort(reverse = True)
print(arr) #['potatoe', 'pineapple', 'orange', 'kiwi', 'cherry', 'carry', 'berry']

#Reverse
arr.reverse()
print(arr) #['berry', 'carry', 'cherry', 'kiwi', 'orange', 'pineapple', 'potatoe']

#Dynamic Array
arr = [1]*5
print(arr)














