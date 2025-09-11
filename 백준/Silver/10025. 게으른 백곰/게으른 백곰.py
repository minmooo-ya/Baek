import sys
input = sys.stdin.readline
N, K = map(int, input().split())
gx = []
for _ in range(N):
    g, x = map(int, input().split())
    gx.append((x, g))
gx.sort()
l = 0
cnt = 0
result = 0
for r in range(N):
    xr, gr = gx[r]
    cnt += gr
    while xr - gx[l][0] > 2*K:
        cnt -= gx[l][1]
        l += 1
    result = max(result, cnt)
print(result)