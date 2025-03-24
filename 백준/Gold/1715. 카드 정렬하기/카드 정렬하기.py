import sys
import heapq

input = sys.stdin.readline

N = int(input())  
N_list = [int(input()) for _ in range(N)]
heapq.heapify(N_list) 
result = 0

while len(N_list) > 1:  # 리스트의 길이가 1보다 클 때까지 반복
    first = heapq.heappop(N_list)  # 가장 작은 값 꺼내기
    second = heapq.heappop(N_list)  # 두 번째로 작은 값 꺼내기
    cost = first + second  # 두 값을 더함
    result += cost  
    heapq.heappush(N_list, cost)  # 다시 힙에 삽입

print(result) 
