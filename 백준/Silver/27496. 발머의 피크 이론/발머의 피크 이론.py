import sys
input = sys.stdin.readline
N, L = map(int, input().split())
a = list(map(int, input().split()))
s = 0
cnt = 0

for i in range(N):
    s += a[i]
    if i >= L:
        s -= a[i - L]
    if 129 <= s <= 138:
        cnt += 1
print(cnt) 