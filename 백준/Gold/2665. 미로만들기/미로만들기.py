# 벽(0)을 지나갈 때 count += 1

# 최종적으로 (N-1, N-1) 위치에서 최소 검은 방을 지나는 횟수를 출력

import sys
import heapq

N = int(sys.stdin.readline().strip())
M = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = 0  # 시작점

q = []
heapq.heappush(q, (0, 0, 0))  # (검은 방을 지나는 횟수, x, y)

while q:
    count, x, y = heapq.heappop(q)
    
    # 목적지 도착 시 최소 검은 방을 지나는 횟수수 출력
    if x == N - 1 and y == N - 1:
        print(count)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            # 다음 위치가 검은 방이면 지나가야 함
            new_count = count + (1 if M[nx][ny] == 0 else 0)

            # 기존보다 검은방을 덜 지나나갈 수 있다면 갱신
            if new_count < dist[nx][ny]:
                dist[nx][ny] = new_count
                heapq.heappush(q, (new_count, nx, ny))

