import sys

N = int(sys.stdin.readline())

# 그래프 생성
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 배열 및 DFS 스택
visited = [0] * (N + 1)

def dfs(node):
    stack = [node]
    while stack:
        top = stack.pop()
        for adj in graph[top]:
            if visited[adj] == 0:
                visited[adj] = top
                stack.append(adj)

dfs(1)

print("\n".join(map(str, visited[2:])))
