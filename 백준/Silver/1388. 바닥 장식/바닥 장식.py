# 세로 - N, 가로 - M
# 총 나무 판자의 개수 출력
# -이면 가로 탐색 / | 이면 세로탐색
# bfs탐색을 하고 나오면 count += 1
# 현재 값 pop하고 유효한 값인지 검사함
# 맞으면 방문처리 and append
import sys
from collections import deque
input = sys.stdin.readline
#bfs탐색
def bfs(x, y, graph, visited, N, M):
    q = deque([(x, y)])
    visited[x][y] = True
    dx, dy = (0, 1) if graph[x][y] == '-' else (1, 0) # 가로 세로 나누기
    
    while q:
        cx, cy = q.popleft()
        nx, ny = cx + dx, cy + dy
        #유효한 값인지 방문했는지 같은 - or  | 인지 체크크
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == graph[cx][cy]:
            visited[nx][ny] = True
            q.append((nx, ny))

#카운트 함수
def count_wood(N, M, wood_list):
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

print(count_wood(N, M, wood_list))
