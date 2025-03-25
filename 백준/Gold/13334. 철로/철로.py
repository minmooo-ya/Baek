import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())  
segments = []

for _ in range(n):
    h, o = map(int, input().split())
    segments.append((min(h, o), max(h, o)))  # 작은 값이 집, 큰 값이 사무실

d = int(input().strip())  # 철로 길이

# 사무실 위치를 기준으로 정렬
segments.sort(key=lambda x: x[1])

# 우선순위 큐 (힙)
heap = []
max_count = 0

# 스위핑 & 우선순위 큐 적용
for start, end in segments:
    heapq.heappush(heap, start)  # 현재 사람의 집 위치 추가

    # 힙의 최솟값(가장 왼쪽 집)이 철로에 포함되지 않으면 제거
    while heap and heap[0] < end - d:
        heapq.heappop(heap)

    # 현재 포함된 사람 수 갱신
    max_count = max(max_count, len(heap))

print(max_count)
