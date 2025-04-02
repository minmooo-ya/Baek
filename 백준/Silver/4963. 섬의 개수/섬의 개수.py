import sys
input = sys.stdin.readline

# 8방향 탐색 (상, 하, 좌, 우, 대각선)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    graph[y][x] = 0  # 시작 지점 방문 처리

    while stack:
        cx, cy = stack.pop()

        for i in range(8):  # 8방향 탐색
            nx, ny = cx + dx[i], cy + dy[i]

            # 유효한 범위 내에서 방문하지 않은 섬(1)만 탐색
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                graph[ny][nx] = 0  # 방문 처리
                stack.append((nx, ny))  # 스택에 추가

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:  # 방문하지 않은 섬이면 DFS 실행
                dfs(x, y)
                count += 1  # 섬 개수 증가

    print(count)
