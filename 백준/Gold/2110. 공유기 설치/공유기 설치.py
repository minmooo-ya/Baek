import sys
N, C = map(int, sys.stdin.readline().split())  
house = [int(sys.stdin.readline()) for _ in range(N)]  
house = sorted(house) 

start = 1 
end = house[-1] - house[0]  # 최대 거리 
result = 0  

while start <= end:
    mid = (start + end) // 2  # 공유기 간 최소 거리 후보
    mile = house[0]  # 첫 번째 집에 공유기 설치
    count = 1  # 공유기 개수 (첫 번째 집에 설치했으니까 1)

    for i in range(1, N):  # 두 번째 집부터
        if house[i] >= mile + mid:  # 현재 집이 마지막 공유기 설치 위치 + mid 거리 이상이면 설치 가능
            mile = house[i]  # 공유기 설치
            count += 1  # 공유기 개수 증가
    if count >= C:
        start = mid + 1  # 더 넓게 배치할 수 있는지
        result = mid  # 가능한 거리 저장
    else:
        end = mid - 1  # 공유기 개수가 부족하면 좁힘

print(result)