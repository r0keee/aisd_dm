from collections import deque
import numpy
def read_as_list(file_path):
    g = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) < 2:
                continue
            node = int(parts[0].strip())
            neighbors = list(map(int, parts[1].strip().split(','))) if parts[1].strip() else []
            g[node] = neighbors
    return g


graph = read_as_list("max_cc.txt") # список смежности максимальной компоненты

def count_edges(graph):
    result = sum(len(n) for n in graph.values())
    return result // 2

def find_min_max_deg(graph):
    result = [float('-inf'), float('inf')]
    degs = []
    for v in graph.keys():
        result[0] = max(result[0], len(graph[v]))
        result[1] = min(result[1], len(graph[v]))
    return result

def get_dist_mat(graph): # с помощью Флойда - Уоршелла
    vertices = sorted(graph.keys())
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}

    dist_matrix = [[1000000000] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist_matrix[i][j] = 0

    for v in graph:
        for u in graph[v]:
            i, j = index[v], index[u]
            dist_matrix[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    return [dist_matrix, vertices]

def dist_rad_dim_ecc(graph):
    dist_matrix, vertices = get_dist_mat(graph)[0], get_dist_mat(graph)[1]

    eccs = [max(row) for row in dist_matrix]
    radius = numpy.min(eccs)
    diameter = numpy.max(eccs)

    center = [vertices[i] for i, e in enumerate(eccs) if e == radius]

    return [dist_matrix, radius, diameter, center]

for row in dist_rad_dim_ecc(graph)[0]:
    print(row)

print(f'Задание 2:')
print(f'|V| = {len(graph.keys())}, |E| = {count_edges(graph)}, 𝛿(G) = {find_min_max_deg(graph)[1]}, '
      f'Δ(G) = {find_min_max_deg(graph)[0]}, rad = {dist_rad_dim_ecc(graph)[1]}, '
      f'diam = {dist_rad_dim_ecc(graph)[2]}, center = {dist_rad_dim_ecc(graph)[3]}, '
      f'цикломатическое число = {count_edges(graph) - len(graph.keys()) + 1}')
