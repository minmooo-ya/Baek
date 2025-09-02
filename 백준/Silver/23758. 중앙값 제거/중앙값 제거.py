import sys
import heapq
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

k = (N + 1) // 2
count = 0

for a in A[:k]:
    while a > 1:
        count += 1
        a = a // 2

print(count + 1)