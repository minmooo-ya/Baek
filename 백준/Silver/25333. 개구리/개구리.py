import sys
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    A, B, X = map(int, input().strip().split())
    a, b = A, B
    while b != 0:
        a, b = b, a%b
        g = a

    print(X//g)