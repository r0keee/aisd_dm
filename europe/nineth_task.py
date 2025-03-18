import heapq

def read_as_list(filename):
    g = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            u, v, weight = int(parts[0]), int(parts[1]), int(parts[2])

            if u not in g:
                g[u] = []
            if v not in g:
                g[v] = []

            g[u].append((v, weight))
            g[v].append((u, weight))

    return g

def prim_find_mst(graph):
    start = 33 # Португалия
    visited = set()
    mst = []
    total = 0

    min_heap = [(0, start, start)]

    while (min_heap):
        w, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)

            if u != v:
                mst.append((u, v, w))
                total += w

            for sosed, e_w in graph[v]:
                if sosed not in visited:
                    heapq.heappush(min_heap, (e_w, v, sosed))

    return [mst, total]


def prim_mst(graph):
    mst = []
    visited = set()
    start_node = next(iter(graph))
    visited.add(start_node)
    edges = [(weight, start_node, v) for v, weight in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for sosed, weight_of_sosed in graph[v]:
                if sosed not in visited:
                    heapq.heappush(edges, (weight_of_sosed, v, sosed))

    return mst

a = set()
edge_list = read_as_list("weights.txt") # список ребер максимальной компоненты с весами
res = prim_find_mst(edge_list)
print(res[0])
print(res[1])
