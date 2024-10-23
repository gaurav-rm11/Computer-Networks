import heapq

def shortestpath(graph, start):
    distances = {node : float ('infinity') for node in graph}
    distances[start] = 0
    priority_q = [(0,start)]

    while(priority_q):
        current_dist, current_node = heapq.heappop(priority_q)

        if current_dist > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            distance = current_dist + weight

            if distance < distances[neighbour]:
                distances[neighbour]=distance
                heapq.heappush(priority_q,(distance, neighbour))

    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(shortestpath(graph, 'A'))
