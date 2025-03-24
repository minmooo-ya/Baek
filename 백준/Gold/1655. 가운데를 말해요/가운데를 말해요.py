import sys
import heapq

input = sys.stdin.readline

N = int(input())  
max_heap = []  
min_heap = [] 

for _ in range(N):
    num = int(input()) 

    # 최대 힙과 최소 힙에 번갈아 가며 넣기
    if not max_heap or num <= -max_heap[0]:  
        heapq.heappush(max_heap, -num)  # 최대 힙은 음수로 저장
    else:
        heapq.heappush(min_heap, num)

    # 최대 힙 크기는 최소 힙보다 같거나 1 더 많아야 함
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

   
    print(-max_heap[0])
