from random import randint

import networkx as nx

from task1 import G

# random generated weights
weights = [49, 68, 96, 79, 39, 41, 74, 43, 18, 92, 80, 75, 70, 64, 29, 52, 62, 27, 99, 77, 18, 14, 44, 44, 17, 16, 39,
           33, 28, 8, 96, 11, 88, 48, 18, 11, 17, 88, 43, 88, 24, 47, 51, 2, 49, 47, 82, 3, 50, 44, 94, 58]


# for i in G.edges():
#     weights.append(randint(1, 100))

num = 0

for i in G.edges():
    G[i[0]][i[1]]['weight'] = weights[num]
    num += 1


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, data in graph[current_vertex].items():
            distance = distances[current_vertex] + data['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


# result = nx.single_source_dijkstra_path_length(G, "Лісова")
result = dijkstra(G, "Лісова")
result = dict(sorted(result.items(), key=lambda x: x[1], reverse=False))
print(result)
