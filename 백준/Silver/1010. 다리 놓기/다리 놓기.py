# dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

dp = [[0] * 31 for _ in range(31)]

for n in range(31):
    dp[n][0] = 1
    for r in range(1, n+1):
        dp[n][r] = dp[n-1][r-1] + dp[n-1][r]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[m][n])