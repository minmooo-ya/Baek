import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) 
M = int(input()) 

graph = {i: [] for i in range(1, N + 1)}
indegree = {i: 0 for i in range(1, N + 1)}
result = [0] * (N + 1)  # 부품 개수 저장 배열


for _ in range(M):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))  # x를 만들기 위해 y가 k개 필요
    indegree[y] += 1  # y의 진입 차수 증가

def toy(graph, indegree, N):
    q = deque()
    q.append(N)  # 완제품부터 시작
    result[N] = 1  # 완제품 하나 필요

    while q:
        curr = q.popleft()  # 현재 부품 꺼내기

        for next_part, K in graph[curr]:
            result[next_part] += result[curr] * K  # 부품 개수 업데이트
            indegree[next_part] -= 1  # 진입 차수 감소

            if indegree[next_part] == 0:
                q.append(next_part)

toy(graph, indegree, N)

for i in range(1, N + 1):
    if not graph[i]: 
        print(i, result[i])
