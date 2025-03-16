import sys

N = int(sys.stdin.readline().strip())  
w = []

for i in range(N):
    w.append(sys.stdin.readline().strip())  

word = list(set(w)) 

word.sort()  
word.sort(key=len)  

for i in word:
    print(i)
