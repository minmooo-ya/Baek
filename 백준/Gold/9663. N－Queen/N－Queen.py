N = int(input())  
count = 0  # 해결 가능한 경우의 수

col_check = [False] * N         
diag1_check = [False] * (2 * N)  # '/' 방향 대각선 체크 (row + col)  
diag2_check = [False] * (2 * N)  # '\' 방향 대각선 체크 (row - col + N)  

def queen(row):
    global count
    if row == N:  
        count += 1
        return
    
    for col in range(N):
        if col_check[col] or diag1_check[row + col] or diag2_check[row - col + N]:  
            continue  # 같은 열 또는 대각선에 퀸이 있으면 넘어감

        # 퀸 배치
        col_check[col] = diag1_check[row + col] = diag2_check[row - col + N] = True
        queen(row + 1)  # 다음 행 탐색
        # 백트래킹 (퀸 제거)
        col_check[col] = diag1_check[row + col] = diag2_check[row - col + N] = False

queen(0)
print(count)
