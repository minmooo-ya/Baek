N = int(input())

dp = [5000] * (N + 1)
dp[0] = 0  # 0kg 만들기 위해 봉지 0개

for i in range(3, N + 1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N] if dp[N] != 5000 else -1)