#정방향 X, 마지막 레벨부터 해야함
#전 레벨 점수 < 다음 레벨 점수
#range를 N-1, 0, -1로 하면 될 듯

import sys
input = sys.stdin.readline
N = int(input().strip())
level = []

for _ in range(N):
    level.append(int(input().strip()))

count = 0
for i in range(N-1, 0, -1):
    a = level[i] -1
    if level[i-1] > a:
        count += level[i-1] - a
        level[i-1] = a
print(count)