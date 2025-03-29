import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}  
indegree = {i: 0 for i in range(1, N + 1)} 

for _ in range(M):
    a, b = map(int, input().split())  # A가 B 앞에 와야 함
    graph[a].append(b)  # A → B 방향 저장
    indegree[b] += 1  # B의 진입 차수 증가

def topological_sort(graph, indegree, N):
    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)


    while q:
        num = q.popleft()
        result.append(num)

        for j in graph[num]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

    print(*result)

topological_sort(graph, indegree, N)
