import sys
input = sys.stdin.readline

N = int(input().strip())
dominoes = []
for _ in range(N):
    a, l = map(int, input().split())
    dominoes.append((a, l))

dominoes.sort()  #정렬
group = 1
for i in range(N-1):
    a_i, l_i = dominoes[i]
    a_next= dominoes[i+1][0]
    if a_next > a_i + l_i:
        group += 1

print(group)