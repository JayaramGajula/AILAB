from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.dfs = " "
        self.found = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, root, search, visited):
        visited.add(root)
        self.dfs = self.dfs + root + " "
        if root == search:
            self.found = True
            return
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, search, visited)

    def DFS(self, root, search):
        visited = set()
        self.DFSUtil(root, search, visited)

g = Graph()
n = int(input("enter the no of nodes"))
root = input("enter the root node")
search = input("enter the search element")
print("enter the vertices of the tree")
for i in range(0, n - 1):
    s = input()
    x = s.split(",")
    g.addEdge(x[0], x[1])

g.DFS(root, search)
if g.found:
    print("following is depth for search")
    print(g.dfs)
else:
    print("given element is not found in the tree")
