import sys
from collections import deque

# BFS 탐색 함수
def bfs(graph, check, start):
    queue = deque([start])
    check[start] = True
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not check[next_node]:
                check[next_node] = True
                queue.append(next_node)

# 연결 요소 개수 구하는 함수
def get_connected_components(N, graph):
    check = [False] * (N + 1)  # 방문 여부 체크
    ans = 0
    
    for node in range(1, N + 1):
        if not check[node]:  # 방문하지 않았다면
            bfs(graph, check, node)  # BFS 탐색
            ans += 1  # 새로운 연결 요소 발견

    return ans

# 입력 받기 (sys.stdin.read()로 최적화)
input = sys.stdin.read
data = input().splitlines()
N, M = map(int, data[0].split())

# 그래프 초기화
graph = {i: [] for i in range(1, N + 1)}  # 1-based 인덱스를 위한 그래프 생성

# 간선 정보 입력 처리
for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    graph[u].append(v)
    graph[v].append(u)  # 방향 없는 그래프이므로 양방향으로 간선 추가

# 연결 요소 개수 출력
print(get_connected_components(N, graph))
