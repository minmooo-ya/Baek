import sys
sys.setrecursionlimit(200000)  # 깊은 재귀를 위한 제한 증가

# DFS 함수 (반복문 방식으로 변경)
def dfs(graph, visited, parent, node):
    stack = [node]
    visited[node] = True
    
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                stack.append(neighbor)

def find_parents(N, edges):
    # 그래프 초기화
    graph = {i: [] for i in range(1, N + 1)}
    
    # 간선 정보 입력
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (N + 1)  # 방문 여부 체크
    parent = [0] * (N + 1)  # 부모 노드를 저장하는 배열
    
    parent[1] = -1  # 루트는 부모가 없으므로 -1로 설정
    dfs(graph, visited, parent, 1)  # 1번 노드를 루트로 DFS 시작
    
    return parent[2:]  # 2번부터 N번 노드까지 부모 노드를 리턴

# 입력 받기
N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

# 부모 노드 찾기
parents = find_parents(N, edges)

# 출력
for p in parents:
    print(p)
