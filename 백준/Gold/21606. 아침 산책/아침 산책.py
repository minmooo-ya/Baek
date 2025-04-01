import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().strip())  # 노드의 수
room_type = list(map(int, input().strip()))  # 실내(1) / 실외(0)
graph = {i: [] for i in range(1, N+1)}

# 트리의 간선 입력
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 처리
visited = [False] * (N + 1)

# DFS 함수
def dfs(node):
    visited[node] = True
    # 현재 노드가 실내라면, 이 노드를 기준으로 연결된 실내 노드만 찾는다.
    for neighbor in graph[node]:
        if not visited[neighbor] and room_type[neighbor - 1] == 1:  # 실내 노드만 탐색
            # 만약 현재 노드와 연결된 실내 노드가 있다면 경로를 찾은 것
            valid_paths.append((node, neighbor))
            dfs(neighbor)

valid_paths = []

# 모든 실내 노드들에 대해 DFS를 돌면서 경로를 찾기
for node in range(1, N + 1):
    if room_type[node - 1] == 1 and not visited[node]:
        dfs(node)

# 유효한 경로 출력
print(len(valid_paths))
