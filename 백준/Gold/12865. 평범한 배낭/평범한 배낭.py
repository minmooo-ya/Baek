import sys
input = sys.stdin.read

lines = input().splitlines()
N, K = map(int, lines[0].split())

items = [tuple(map(int, line.split())) for line in lines[1:]]

# 1차원 DP 배열
dp = [0] * (K + 1)

for w, v in items:
    # 0/1 Knapsack은 뒤에서부터 순회
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])
