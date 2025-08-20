from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A,1))
visited = set()
visited.add(A)

answer = -1

while q:
    x, cnt = q.popleft()
    if x == B:
        answer = cnt
        break
    nx = x*2
    if nx <= B and nx not in visited:
        visited.add(nx)
        q.append((nx, cnt + 1))
    nx = x*10+1
    if nx <= B and nx not in visited:
        visited.add(nx)
        q.append((nx, cnt + 1))

print(answer)