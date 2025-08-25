import sys
input = sys.stdin.readline
N = int(input().strip())
A = list(map(int, input().strip().split()))
INF = 10**19
dp = [INF]*N
dp[0] = 0
for j in range(1, N):
    aj = A[j]
    best = INF
    for i in range(j):
        cost = (j-i) * (1 + abs(A[i] - aj))
        K = max(dp[i], cost)
        if K < best:
            best = K
    dp[j] = best
print(dp[-1])