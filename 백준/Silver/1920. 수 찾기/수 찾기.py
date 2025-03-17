import sys


N = int(sys.stdin.readline().strip())  
A = set(map(int, sys.stdin.readline().split())) 

M = int(sys.stdin.readline().strip())  
B = list(map(int, sys.stdin.readline().split()))


for num in B:
    print(1 if num in A else 0) 
