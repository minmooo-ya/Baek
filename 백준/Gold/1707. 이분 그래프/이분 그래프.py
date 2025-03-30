# 입력 받아 그래프 생성

# colors 리스트를 만들어 방문 여부 및 색깔(0: 미방문, -1, 1) 저장

# 모든 정점을 돌면서 방문하지 않은 정점이면 DFS 시작

# DFS 탐색하면서 현재 정점과 반대 색으로 다음 정점 색칠

# 만약 방문한 정점인데 같은 색이면 이분그래프 아님

import sys

input = sys.stdin.readline

def dfs(V, graph):
    color = [0] * (V+1)

    for i in range(1, V + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1

            while stack:
                node = stack.pop()
                for next_node in graph[node]:
                    if color[next_node] == 0:
                        color[next_node] = -color[node]
                        stack.append(next_node)
                    elif color[next_node] == color[node]:
                        return False
    return True 

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    if dfs(V, graph):
        print("YES")
    else:
        print("NO")