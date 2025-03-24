import sys
from collections import deque

input = sys.stdin.readline

# 보드 크기 (N x N)
N = int(input())

# 사과 위치 저장 (집합 사용 → 빠르게 탐색 가능)
K = int(input()) #사과 개수
apples = set() # 사과 위치
for _ in range(K): 
    x, y = map(int, input().split())
    apples.add((x - 1, y - 1))  # 0-indexed로 변환

# 방향 전환 정보 저장 (딕셔너리 사용)
L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 방향 (오른쪽, 아래, 왼쪽, 위)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0  # 처음에는 오른쪽 (directions[0])

# 뱀의 초기 위치
snake = deque([(0, 0)])

# 게임 실행
time = 0  # 시간
while True:
    time += 1  # 1초 증가

    #머리를 이동
    head_x, head_y = snake[-1]
    dx, dy = directions[current_direction]
    new_x, new_y = head_x + dx, head_y + dy

    #벽에 부딪히거나 자기 몸과 충돌하면 종료
    if not (0 <= new_x < N and 0 <= new_y < N) or (new_x, new_y) in snake:
        break

    #이동한 위치가 사과인지 확인
    snake.append((new_x, new_y))  # 머리 추가
    if (new_x, new_y) in apples:
        apples.remove((new_x, new_y))  # 사과 먹기
    else:
        snake.popleft()  # 사과 없으면 꼬리 제거

    #방향 전환이 있는지 확인
    if time in turns:
        if turns[time] == 'L':  # 왼쪽 회전
            current_direction = (current_direction - 1) % 4
        else:  # 오른쪽 회전
            current_direction = (current_direction + 1) % 4

# 게임이 끝난 시간 출력
print(time)
