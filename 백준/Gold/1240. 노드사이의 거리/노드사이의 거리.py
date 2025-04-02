import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, end):
    q = deque([(start, 0)])
    visited = set()

    while q:
        node, dist = q.popleft()
        if node == end:
            return dist
        visited.add(node)

        for neigbor, weight in graph[node]:
            if neigbor not in visited:
                q.append((neigbor, dist + weight))

    return -1

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N-1):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

for _ in range(M):
    start, end = map(int, input().split())
    print(bfs(graph, start, end))