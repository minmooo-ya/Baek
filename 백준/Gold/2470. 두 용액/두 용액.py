import sys
import bisect

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

A.sort()

a_sum = float('inf')  
answer = (0, 0)  

# 이분 탐색을 사용하여 최적의 두 용액 찾기
for i in range(N - 1):  # 마지막 원소는 비교 대상이 없으니까 N-1까지
    target = -A[i]  # 현재 값 A[i]의 반대값을 찾기

    # A[i] 이후의 부분에서 target과 가장 가까운 값 찾기
    idx = bisect.bisect_left(A, target, i + 1)  # A[i+1:]에서 target의 위치 찾기

    # idx가 범위 내에 있는 경우 비교
    if idx < N and abs(A[i] + A[idx]) < abs(a_sum):
        a_sum = A[i] + A[idx]
        answer = (A[i], A[idx])

    # idx-1도 범위 내에 있다면 비교 
    if i + 1 <= idx - 1 and abs(A[i] + A[idx - 1]) < abs(a_sum):
        a_sum = A[i] + A[idx - 1]
        answer = (A[i], A[idx - 1])

# 결과 출력
print(answer[0], answer[1])
