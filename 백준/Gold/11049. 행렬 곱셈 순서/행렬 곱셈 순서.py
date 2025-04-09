import sys

input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

# dp[i][j] = i번째부터 j번째까지 곱하는 최소 연산 수
dp = [[0] * n for _ in range(n)]

# 행렬 체인 길이 (2개, 3개, ..., n개짜리 구간)
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        
        # i부터 j까지 중간에 어디서 끊을지 선택
        for k in range(i, j):
            cost = (dp[i][k] + dp[k + 1][j] +
                    matrix[i][0] * matrix[k][1] * matrix[j][1])
            dp[i][j] = min(dp[i][j], cost)

# 전체 행렬을 곱하는 최소 연산 수 출력
print(dp[0][n - 1])
