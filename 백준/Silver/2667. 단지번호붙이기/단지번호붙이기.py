# 단지수 , 단지 내 집 수 출력
# #범위를 벗어나면 종료
# 0을 만나면 종료
# 이미 방문한 1을 만나면 종료
# 1을 만나면 탐색시작, 연결된 모든 1 방문처리하고 카운트
import sys
input = sys.stdin.readline

N = int(input())
N_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)] 

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:  # 범위 벗어나면 종료
        return 0
    if visited[x][y] or N_list[x][y] == 0:  # 이미 방문했거나 0이면 종료
        return 0
    
    visited[x][y] = True  
    count = 1  

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        count += dfs(x + dx[i], y + dy[i])

    return count

#모든 위치에서 DFS 실행하여 단지 개수 찾기
complexes = []  # 각 단지 내 집 개수를 저장할 리스트

for i in range(N):
    for j in range(N):
        if N_list[i][j] == 1 and not visited[i][j]:  # 방문하지 않은 1이면 새 단지 시작
            complexes.append(dfs(i, j))

print(len(complexes))
for c in sorted(complexes):  # 단지 크기 오름차순 정렬 후 출력
    print(c)
