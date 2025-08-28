#중간점 잡고 왼 오 합 같으면 갱신
import sys
input = sys.stdin.readline
S = input().strip()
n = len(S)
A = [int(ch) for ch in S]
ans = 0

for L in range(2, n+1, 2):
    for s in range(0, n-L+1):
        mid = s + L//2
        left = A[s:mid]
        right = A[mid:s+L]
        if sum(left) == sum(right):
            ans = max(ans, L)
print(ans)