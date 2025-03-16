from itertools import permutations
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))


max_a = 0
for perm in permutations(arr):
    total_sum = sum(abs(perm[i] - perm[i + 1]) for i in range(n - 1))
    max_a = max(max_a, total_sum)

# 최댓값 출력
print(max_a)
