import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.reverse()  # 큰 동전부터 탐색

count = 0
for coin in coins:
    if k == 0:
        break
    count += k // coin  # 현재 동전으로 몇 개 쓸 수 있는지
    k %= coin

print(count)