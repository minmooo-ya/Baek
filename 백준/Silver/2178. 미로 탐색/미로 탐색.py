import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# BFS 함수
def bfs(graph, start):
    queue = deque([start])  
    graph[start[0]][start[1]] = 1  # 시작점을 1로 설정 (첫 번째 칸 포함)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
    
        if x == N - 1 and y == M - 1:
            return graph[x][y]
        
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
           
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny)) 
    
    return -1  


start = (0, 0)

result = bfs(graph, start)

print(result)
