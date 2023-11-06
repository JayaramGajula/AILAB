from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs = " "
        self.found = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFSUtil(self, root, search, visited):
        queue = []
        visited.add(root)
        queue.append(root)
        while queue:
            m = queue.pop(0)
            self.bfs += m + " "
            if m == search:
                self.found = True
                return
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def BFS(self, root, search):
        visited = set()
        self.BFSUtil(root, search, visited)


g = Graph()
n = int(input("enter the no of nodes: "))
root = input("enter the root node: ")
search = input("enter the search element: ")
print("enter the vertices of the tree:")
for i in range(0, n - 1):
    s = input()
    x = s.split(",")
    g.addEdge(x[0], x[1])

g.BFS(root, search)
if g.found:
    print("following is breadth-first search:")
    print(g.bfs)
else:
    print("given element is not found in the tree")
