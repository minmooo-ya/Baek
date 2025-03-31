# N개의 도시 -> 정점
# M개의 버스 -> 간선
# A->B(A,B,W)
# 출발점, 도착점

import sys
import heapq
input = sys.stdin.readline

def mincost(graph, N, M, s, e):
    distances = [float('inf')] * (N+1)
    distances[s] = 0

    pq = [(0,s)]

    while pq:
        c_d, c_n = heapq.heappop(pq)

        if c_d > distances[c_n]:
            continue
        
        for neighbor, weight in graph[c_n]:
            new_distances = c_d + weight

            if new_distances < distances[neighbor]:
                distances[neighbor] = new_distances
                heapq.heappush(pq, (new_distances, neighbor))

    return print(distances[e])

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, e = map(int, input().split())

mincost(graph, N, M, s, e)