import sys

input = sys.stdin.readline

K = int(input().strip())
stack = []

for _ in range(K):
    num = int(input().strip())  

    if num == 0:  
        if stack:  # 스택이 비어있지 않으면 pop
            stack.pop()
    else:
        stack.append(num) 

print(sum(stack))  
