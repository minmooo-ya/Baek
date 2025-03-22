import sys
import heapq

input = sys.stdin.readline

N = int(input())
max_heap = []
result = []

for _ in range(N):
    N_list = int(input().strip())

    if N_list == 0:
        if max_heap:
            result.append(heapq.heappop(max_heap)[1]) 
        else:
            result.append(0)
    else:
        heapq.heappush(max_heap, (-N_list, N_list)) 

print("\n".join(map(str, result)))