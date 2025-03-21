import sys
input = sys.stdin.readline

# 부분수열 = []  # LIS를 저장할 배열

# for 현재값 in 원래배열:
#     만약 부분수열이 비었거나 현재값이 부분수열의 마지막 값보다 크다면:
#         부분수열에 현재값 추가
#     아니라면:
#         부분수열에서 현재값이 들어갈 위치를 이분 탐색으로 찾고, 해당 위치 값 변경

# LIS 길이 = len(부분수열)
import sys
input = sys.stdin.readline

def binary_search(partition_A, target):  #이분 탐색색

    st, en = 0, len(partition_A) - 1
    while st <= en:
        mid = (st + en) // 2
        if partition_A[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return st  # target이 들어갈 자리

def LIS(A):                             # 가장 긴 증가하는 부분수열 구하기기
    partition_A = []  # 부분수열 리스트

    for num in A:
        if not partition_A or num > partition_A[-1]:  
            partition_A.append(num)  # 증가하는 경우 추가
        else:
            idx = binary_search(partition_A, num)  # 적절한 위치 찾기
            partition_A[idx] = num  # 기존 값을 변경

    return len(partition_A)  



N = int(input().strip())  
A = list(map(int, input().split()))  

print(LIS(A))
  