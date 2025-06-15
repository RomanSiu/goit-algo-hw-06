from collections import deque

from task1 import G, show_graph


def bfs_recursive(graph, queue, visited=None):
    bfs_queue = []
    if visited is None:
        visited = set()

    if not queue:
        return

    vertex = queue.popleft()

    if vertex not in visited:
        bfs_queue.append(vertex)
        # print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    que = bfs_recursive(graph, queue, visited)
    if que is not None:
        bfs_queue.extend(que)
    return bfs_queue


def dfs_recursive(graph, vertex, visited=None):
    dfs_queue = []
    if visited is None:
        visited = set()
    visited.add(vertex)
    dfs_queue.append(vertex)
    # print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            que = dfs_recursive(graph, neighbor, visited)
            if que is not None:
                dfs_queue.extend(que)
    return dfs_queue


bfs_order = bfs_recursive(G, deque(["Лісова"]))
dfs_order = dfs_recursive(G, "Лісова")


def add_labels(order, title):
    for i in range(len(order)):
        G.nodes[order[i]]["order"] = i+1

    node_labels = {node: f"{node} - {data['order']}" for node, data in G.nodes(data=True)}
    show_graph(G, {"labels": node_labels, "title": title})


add_labels(bfs_order, "BFS")
print("Можна побачити що при цьому варіанті обхід відбувається почергово в кожній гілці.")
add_labels(dfs_order, "DFS")
print("При DFS можна побачити що обхід відбувається по гілкам.")
