import sys
sys.setrecursionlimit(10**6)  # DFS 재귀 깊이 설정

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if safe_check[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)

# 입력 처리
N = int(sys.stdin.readline().strip())
N_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_N = max(map(max, N_list))  # 최대 높이 찾기

max_safe_area = 0  # 최대 안전 영역 개수 저장

# 탐색 
for height in range(0, max_N + 1):
    visited = [[False] * N for _ in range(N)]
    safe_check = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if N_list[i][j] > height:  # 현재 높이보다 높은 지역만 살아남음
                safe_check[i][j] = True

    count = 0
    for i in range(N):
        for j in range(N):
            if safe_check[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1

    max_safe_area = max(max_safe_area, count)

print(max_safe_area)
