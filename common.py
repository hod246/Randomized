import time


def modified_dijkstra(G, source, i, Lambda):
    assert source in G.nodes, "Such source node doesn't exist"

    # 1. Mark all nodes unvisited and store them.
    # 2. Set the distance to zero for our initial node
    # and to infinity for other nodes.
    distances = {vertex: float('inf') for vertex in G.nodes}
    previous_vertices = {vertex: None for vertex in G.nodes}
    distances[source] = 0
    vertices = dict(G.nodes).copy()

    while vertices:
        # 3. Select the unvisited node with the smallest distance,
        # it's current node now.
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])

        # 6. Stop, if the smallest distance
        # among the unvisited nodes is infinity.
        if distances[current_vertex] == float('inf'):
            break

        # 4. Find unvisited neighbors for the current node
        # and calculate their distances through the current node.
        for neighbour in G[current_vertex]:
            weight = G[current_vertex][neighbour]['weight']
            alternative_route = distances[current_vertex] + weight

            # Compare the newly calculated distance to the assigned
            # and save the smaller one.
            if alternative_route < Lambda[i + 1][current_vertex]:  # modification of dijkstra
                distances[neighbour] = min(alternative_route, distances[neighbour])
                previous_vertices[neighbour] = current_vertex

        # 5. Mark the current node as visited
        # and remove it from the unvisited set.
        vertices.pop(current_vertex)
    return distances


def avg(input_list):
    return sum(input_list) / len(input_list)


def average_difference(list1, list2):
    return avg([i / j for i, j in zip(list1, list2) if j != 0])


def timeit(method, log_name=None, output=None):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        if output is not None:
            output[log_name if log_name is not None else method.__name__] = (te - ts) * 1000
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result

    return timed
