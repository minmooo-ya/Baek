import sys
from collections import deque

input = sys.stdin.readline

dz = [0, 0, 0, 0, 1, -1]  # 위, 아래 추가
dy = [-1, 1, 0, 0, 0, 0]  # 상, 하
dx = [0, 0, -1, 1, 0, 0]  # 좌, 우


def bfs():
    q = deque()
    day = -1

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] ==1:
                    q.append((z,y,x))

    while q:
        day += 1
        for _ in range(len(q)):
            z, y, x = q.popleft()


            for i in range(6):
                nz, ny, nx = z + dz[i], y+dy[i], x + dx[i]
                if 0 <= nz <H and 0 <= ny < N and 0 <= nx < M and graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    q.append((nz,ny,nx))

    if any(0 in row for box in graph for row in box):
        return -1
    return day

M, N, H = map(int,input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs())