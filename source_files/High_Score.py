n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, x = map(int, input().split())
    edges.append((a, b, x))

graph = [[] for _ in range(n + 1)]
for a, b, _ in edges:
    graph[a].append(b)

INF = float('-inf')
scores = [INF] * (n + 1)
scores[1] = 0

for i in range(n - 1):
    updated = False
    for a, b, x in edges:
        if scores[a] != INF and scores[a] + x > scores[b]:
            scores[b] = scores[a] + x
            updated = True

    if not updated:
        break

potential_cycle_vertices = set()

for _ in range(n):
    for a, b, x in edges:
        if scores[a] != INF and scores[a] + x > scores[b]:
            scores[b] = scores[a] + x
            potential_cycle_vertices.add(b)
            potential_cycle_vertices.add(a)

if not potential_cycle_vertices:
    print(scores[n])
    exit()

def is_reachable(start, end):
    visited = [False] * (n + 1)
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        
        if current == end:
            return True
        
        if visited[current]:
            continue
        
        visited[current] = True
        
        for next_node in graph[current]:
            if not visited[next_node]:
                queue.append(next_node)
    
    return False

for vertex in potential_cycle_vertices:
    if is_reachable(vertex, n):
        print(-1)
        exit()

print(scores[n])