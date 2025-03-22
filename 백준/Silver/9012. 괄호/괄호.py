import sys

input = sys.stdin.readline
T = int(input().strip())  

for i in range(T): 
    stack = []  
    V = input().strip()  
    
    for char in V:
        if char == '(':
            stack.append('(')
        else:
            if not stack:
                print('NO')
                break  
            stack.pop()
    else: 
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
