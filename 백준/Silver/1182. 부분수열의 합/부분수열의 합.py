import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(a, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)