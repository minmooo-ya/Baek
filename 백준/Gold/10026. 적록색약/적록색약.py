# flodd fill 
# 구역 개수, 적록색약 구역 수 출력
# 적록색약 구역 수 -> G를 R로 바꿔서 
import sys
input = sys.stdin.readline

def red_green(graph):
    visited = [[False] * N for _ in range(N)]
    count = 0  

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 방문하지 않은 새로운 구역
                stack = [(i, j)]
                visited[i][j] = True
                color = graph[i][j]  # 현재 구역의 색

                while stack:
                    x, y = stack.pop()
                    
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # 상하좌우 탐색
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if graph[nx][ny] == color:  # 같은 색이면 탐색 진행
                                visited[nx][ny] = True
                                stack.append((nx, ny))

                count += 1

    return count

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

# 적록색약 그래프 생성 (G → R 변환)
blind_graph = [[cell if cell != 'G' else 'R' for cell in row] for row in graph]

# 일반 구역 개수
normal_count = red_green(graph)

# 적록색약 구역 개수
green_count = red_green(blind_graph)

print(normal_count, green_count)
