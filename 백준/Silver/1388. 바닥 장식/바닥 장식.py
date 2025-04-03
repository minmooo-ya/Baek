# 세로 - N, 가로 - M
# 총 나무 판자의 개수 출력
from collections import deque

def bfs(x, y, graph, visited, N, M):
    queue = deque([(x, y)])
    visited[x][y] = True
    dx, dy = (0, 1) if graph[x][y] == '-' else (1, 0)
    
    while queue:
        cx, cy = queue.popleft()
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == graph[cx][cy]:
            visited[nx][ny] = True
            queue.append((nx, ny))

def count_panels(N, M, wood_list):
    visited = [[False] * M for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                bfs(i, j, wood_list, visited, N, M)
                count += 1

    return count

N, M = map(int, input().split())
wood_list = [list(input().strip()) for _ in range(N)]

print(count_panels(N, M, wood_list))
