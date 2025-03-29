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
        count += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor]:  
                visited[neighbor] = True  
                queue.append(neighbor)    

    return count-1


print(bfs(1))
