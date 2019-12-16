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
