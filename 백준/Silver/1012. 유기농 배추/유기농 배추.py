import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:  # 범위 벗어나면 종료
        return
    if field[y][x] == 0:  # 배추가 없으면 종료
        return

    field[y][x] = 0  # 방문 처리 (visited 배열 없이 배추밭 자체를 수정)

    # 상, 하, 좌, 우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        dfs(x + dx[i], y + dy[i])

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  # 배추밭 크기 (M x N), 배추 개수(K)
    field = [[0] * M for _ in range(N)]  # 배추밭 초기화

    for _ in range(K):
        x, y = map(int, input().split())  
        field[y][x] = 1  # 배추가 있는 곳을 1로 표시

    count = 0  # 필요한 지렁이 수

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:  # 방문하지 않은 배추라면
                dfs(j, i)  # DFS 탐색
                count += 1  # 배추 덩어리 개수 증가

    print(count)  # 결과 출력
