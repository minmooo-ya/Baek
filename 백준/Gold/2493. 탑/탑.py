import sys

input = sys.stdin.readline

N = int(input().strip())    
h = list(map(int, input().split()))  

stack = []
result = [] #신호받을 탑 인덱스

for i in range(N):
    while stack and stack[-1][0] < h[i]:  #현재 값보다 작으면 의미 없으니까 pop
        stack.pop() 
    if stack:
        result.append(stack[-1][1] + 1)
    else:
        result.append(0)

    stack.append((h[i], i))  # 현재 탑을 스택에 추가

print(*result)