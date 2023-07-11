arr = ["apple", "banana", "cherry","berry","carry"]

#Slicing (start-included : end-excluded)
print(arr[0:1]) #['apple']
print(arr[1:2]) #['potatoe', 'pineapple', 'orange', 'kiwi', 'cherry', 'carry', 'berry']

#slicing (start-included : n)
print(arr[1:])  #['banana', 'cherry', 'berry', 'carry']

#slicing (0: end-excluded)
print(arr[:2])  #['apple', 'banana']

#slicing-reverse (0: end-included)
print(arr[:-1])  #['apple', 'banana', 'cherry', 'berry']

#slicing-reverse (start-excluded : end-included)
print(arr[-3:-1])  #['cherry', 'berry']