import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())
A = list(map(int, input().split()))
left = 0
right = max(A)
while left <= right:
    mid = (left + right) // 2
    candy = 0
    for a in A:
        if a > mid:
            candy += (a - mid)
        if candy > K:
            break
    if candy <= K:
        right = mid - 1
    else:
        left = mid + 1
print(left)