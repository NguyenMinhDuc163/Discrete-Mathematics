import math
import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

def DFS(v, visited, graph):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            DFS(neighbor, visited, graph)

def countConnectedComponents(graph):
    visited = [False] * len(graph)
    count = 0

    for v in range(len(graph)):
        if not visited[v]:
            count += 1
            DFS(v, visited, graph)

    return count

with open('input.txt', 'r') as f:
    n, d = map(int, f.readline().split())
    vertices = []
    for i in range(n):
        x, y = map(int, f.readline().split())
        vertices.append((x, y))

    G = [[] for i in range(n)]
    isolated = set(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi = vertices[i]
            xj, yj = vertices[j]
            dist = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
            if dist <= d:
                G[i].append(j)
                G[j].append(i)
                if i in isolated:
                    isolated.remove(i)
                if j in isolated:
                    isolated.remove(j)

    num_components = countConnectedComponents(G)

    if isolated:
        num_components += len(isolated)

    print("Số thành phần liên thông là:", num_components)

    # Vẽ đồ thị
    gv = GraphVisualization()
    for i in range(n):
        for j in G[i]:
            gv.addEdge(i, j)
    for i in isolated:
        gv.addEdge(i, i)
    gv.visualize()
