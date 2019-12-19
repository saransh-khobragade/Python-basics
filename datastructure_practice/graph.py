graph = {
    "A":set(["B","G"]),
    "B":set(["A","C","D","E"]),
    "C":set(["H"]),
    "D":set(["G","B"]),
    "E":set(["F"]),
    "F":set(["E","H"]),
    "G":set(["D","F"]),
    "H":set(["C"])
}

#BFS
def bfs(graph,start):
    visited = set()
    queque = [start]

    while queque:
        vertex = queque.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queque.extend(graph[vertex] - set(visited))
    return visited
print(bfs(graph,"A"))

#DFS
def dfs(graph,start):
    visited = set()
    queque = [start]

    while queque:
        vertex = queque.pop()  #just changes here 
        if vertex not in visited:
            visited.add(vertex)
            queque.extend(graph[vertex] - set(visited))
    return visited
print(dfs(graph,"A"))

#append add a list at the end of list like [1,3,4,[4,5]]
#extend add elements of that list one by one at the end


#BFS path
def bfs_path(graph,start,end):
    queque = [(start,[start])]
    while queque:
        (vertice,path) = queque.pop(0)

        for x in graph[vertice] - set(path):
            if x == end:
                yield path + [x]
            else:
                queque.append((x,path+[x]))

print(list(bfs_path(graph,'A','F')))

#BFS shortest path
def bfs_shortest_path(graph,start,end):
    try:
        return next(bfs_path(graph,start,end))
    except StopIteration:
        return None

print(bfs_shortest_path(graph,'A','H'))