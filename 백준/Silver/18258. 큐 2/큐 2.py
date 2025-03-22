import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())    
queue = deque()  

def push(p):
    queue.append(p)  

def pop():
    if queue:
        print(queue.popleft())  
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    print(1 if not queue else 0)

def front():
    print(queue[0] if queue else -1)

def back():
    print(queue[-1] if queue else -1)

for _ in range(N):  
    command = input().split()
    if command[0] == 'push':
        push(int(command[1]))  
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
