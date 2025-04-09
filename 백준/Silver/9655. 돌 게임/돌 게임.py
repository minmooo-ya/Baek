# dp[i] = not dp[i-1] or not dp[i-3]
# True면 상근이 이기는 상태, False면 창영이 이김

N = int(input())

dp = [False] * (N + 4)  # 최대 N+3까지 필요할 수 있음
dp[1] = True   # 상근 승
dp[2] = False  # 창영 승
dp[3] = True   # 상근 승

for i in range(4, N + 1):
    dp[i] = not dp[i - 1] or not dp[i - 3]

print("SK" if dp[N] else "CY")