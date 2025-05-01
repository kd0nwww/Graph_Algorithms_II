import heapq 

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float('inf')
distances = [INF] * (n + 1)
distances[1] = 0

priority_queue = [(0, 1)] 

visited = [False] * (n + 1)

while priority_queue:
    current_distance, current_city = heapq.heappop(priority_queue)
    
    if visited[current_city]:
        continue
    
    visited[current_city] = True
    
    for neighbor, weight in graph[current_city]:
        if distances[current_city] + weight < distances[neighbor]:
            distances[neighbor] = distances[current_city] + weight
            heapq.heappush(priority_queue, (distances[neighbor], neighbor))

print(' '.join(map(str, distances[1:])))