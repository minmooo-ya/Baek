from collections import deque

N = int(input())
C = int(input())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(C):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

def bfs(start):
    queue = deque([start])  
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft() 
        count += 1  # 방문한 노드 수 증가

        # 현재 노드와 연결된 모든 노드 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:  # 아직 방문하지 않은 노드라면
                visited[neighbor] = True  # 방문 처리
                queue.append(neighbor)    # 큐에 추가

    return count

result = bfs(1)

print(result - 1)
