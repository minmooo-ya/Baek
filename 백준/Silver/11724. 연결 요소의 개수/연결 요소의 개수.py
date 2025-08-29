#bfs
import sys
from collections import deque
inout = sys.stdin.readline

N, M = map(int, inout().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, inout().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (N+1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        q=deque()
        visited[i] = 1
        q.append(i)
        while q:
            cur = q.popleft()
            for j in graph[cur]:
                if not visited[j]:
                    visited[j] = 1
                    q.append(j)
        count += 1
print(count)