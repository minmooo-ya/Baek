import sys

input = sys.stdin.readline
N = int(input().strip())    
h = [int(input().strip()) for _ in range(N)]
stack = [h[-1]]
for i in range(N-2, -1, -1): 
    if h[i] > stack[-1]:
        stack.append(h[i])

print(len(stack))
