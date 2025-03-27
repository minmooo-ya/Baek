from collections import deque

def DFS(graph, visited, v):
    visited[v] = True  
    print(v, end=" ")  
    
    # v와 연결된 노드들을 모두 탐색 (정렬된 상태에서)
    for next_v in sorted(graph[v]):
        if not visited[next_v]:  # 아직 방문하지 않은 노드일 경우
            DFS(graph, visited, next_v)  # 재귀적으로 DFS 호출


def BFS(graph, visited, start):
    queue = deque([start])  # 시작 노드를 큐에 넣기
    visited[start] = True  # 시작 노드를 방문 처리

    while queue:
        # 큐에서 노드 꺼내기
        cur = queue.popleft()  # 큐의 앞에서 노드를 꺼냄
        print(cur, end=" ")  # 현재 노드 출력

        # 현재 노드에 인접한 모든 노드를 탐색
        for neighbor in sorted(graph[cur]):  # 인접 노드를 정렬해서 순차적으로 탐색
            if not visited[neighbor]:  # 아직 방문하지 않은 노드라면
                visited[neighbor] = True  # 방문 처리
                queue.append(neighbor)  # 큐에 넣기


# 입력 처리
N, M, V = map(int, input().split())

# 그래프 초기화 (1부터 N까지 사용)
graph = [[] for _ in range(N+1)]

# 간선 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부를 나타내는 리스트 (1부터 N까지 사용)
visited_bfs = [False] * (N + 1)
visited_dfs = [False] * (N + 1)

# DFS 실행
DFS(graph, visited_dfs, V)
print()  # DFS와 BFS를 구분하기 위한 줄바꿈

# BFS 실행
BFS(graph, visited_bfs, V)
