import sys
input = sys.stdin.readline
P, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
count = 0
for i in A:
    if P < 200:
        count += 1
        P += i
    else:
        break
print(count)