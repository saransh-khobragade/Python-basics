a = set((1,2,3,4))
b = set()

b.add(4)
b.add(6)

print(a & b)
#common element

#diff
print(a-b)

s = set((1, 2, 3))  # create set from tuple
print(s)            # { 1, 2, 3}

s = set([1, 2, 3])  # create set from list
print(s)            # { 1, 2, 3}

s = set('ABC')      # create set from string
print(s)            # {'C', 'B', 'A'}
