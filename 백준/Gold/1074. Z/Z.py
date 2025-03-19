import sys
def Z (N, r, c):
    if N == 0:
        return 0
    

    mid = 2**(N-1)
    if r < mid and c < mid:  # 1사분면
        return Z(N-1, r, c)
    elif r < mid and c >= mid:  # 2사분면
        return mid * mid + Z(N-1, r, c - mid)
    elif r >= mid and c < mid:  # 3사분면
        return 2 * mid * mid + Z(N-1, r - mid, c)
    else:  # 4사분면
        return 3 * mid * mid + Z(N-1, r - mid, c - mid)



N, r, c = map(int, sys.stdin.readline().split())
print(Z(N,r,c))