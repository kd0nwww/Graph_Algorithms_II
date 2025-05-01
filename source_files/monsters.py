from collections import deque

n, m = map(int, input().split())

labyrinth = []
for _ in range(n):
    labyrinth.append(list(input()))

start_x, start_y = 0, 0
monsters = []

for i in range(n):
    for j in range(m):
        if labyrinth[i][j] == 'A':
            start_x, start_y = i, j
        elif labyrinth[i][j] == 'M':
            monsters.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
direction_chars = ['D', 'U', 'L', 'R']

visited = [[False] * m for _ in range(n)]
visited[start_x][start_y] = True

prev_step = [[-1] * m for _ in range(n)]

monster_dist = [[float('inf')] * m for _ in range(n)]
monster_queue = deque()

for mx, my in monsters:
    monster_dist[mx][my] = 0
    monster_queue.append((mx, my))

while monster_queue:
    mx, my = monster_queue.popleft()
    
    for i in range(4):
        nx, ny = mx + dx[i], my + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and labyrinth[nx][ny] != '#' and monster_dist[nx][ny] == float('inf'):
            monster_dist[nx][ny] = monster_dist[mx][my] + 1
            monster_queue.append((nx, ny))

if (start_x == 0 or start_y == 0 or start_x == n - 1 or start_y == m - 1) and monster_dist[start_x][start_y] > 0:
    print("YES")
    print("0")
    print("")
    exit()

queue = deque([(start_x, start_y, 0)])
found_exit = False
exit_pos = (-1, -1)

while queue and not found_exit:
    x, y, steps = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if (0 <= nx < n and 0 <= ny < m and 
            labyrinth[nx][ny] != '#' and 
            not visited[nx][ny] and 
            steps + 1 < monster_dist[nx][ny]):
            
            prev_step[nx][ny] = i
            visited[nx][ny] = True
            
            if nx == 0 or ny == 0 or nx == n - 1 or ny == m - 1:
                found_exit = True
                exit_pos = (nx, ny)
                break
            
            queue.append((nx, ny, steps + 1))

if found_exit:
    path = []
    x, y = exit_pos
    while (x, y) != (start_x, start_y):
        step_idx = prev_step[x][y]
        path.append(direction_chars[step_idx])
        x -= dx[step_idx]
        y -= dy[step_idx]
    
    path.reverse()
    
    print("YES")
    print(len(path))
    print(''.join(path))
else:
    print("NO")