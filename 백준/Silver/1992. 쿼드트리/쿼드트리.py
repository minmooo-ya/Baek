import sys
input = sys.stdin.readline

def tree(x, y, size):
    f_N = N_list[x][y]  # 초기 값

    for i in range(x, x + size):
        for j in range(y, y + size):
            if N_list[i][j] != f_N:  # 다른 값이 나오면 분할
                mid = size // 2
                print("(", end="") 
                tree(x, y, mid)  # 2사분면
                tree(x, y + mid, mid)  # 1사분면
                tree(x + mid, y, mid, )  # 3사분면
                tree(x + mid, y + mid, mid)  # 4사분면
                print(")", end="") 
                return
            
    print(f_N, end="")  


N = int(input())
N_list = [list(map(int, input().strip())) for _ in range(N)] 


tree(0, 0, N)  
