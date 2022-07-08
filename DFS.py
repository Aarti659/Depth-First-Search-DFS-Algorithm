graph1 = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
    'H': ['E', 'G'],
    'S': ['A', 'C', 'G']
}


def de_fi_se(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for j in graph[node]:
            de_fi_se(graph, j, visited)
    return visited


visited = de_fi_se(graph1, 'A', [])
print(visited)



