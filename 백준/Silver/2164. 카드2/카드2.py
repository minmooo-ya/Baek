from collections import deque

N = int(input())
N_Q = deque(range(1, N + 1)) 

while len(N_Q) > 1:
    N_Q.popleft()  # 맨 앞 제거
    N_Q.append(N_Q.popleft())  # 그다음 요소를 맨 뒤로 이동

print(N_Q[0])
