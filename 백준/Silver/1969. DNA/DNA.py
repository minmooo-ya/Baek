#열기준 빈도 수 높은 애 뽑기 
#-> 가장 차이가 적어야하면 각 DNA에서 열마다 많은 애를 뽑으면 차이가 젤 적지 않나..
#딕셔너리로 빈도수 체크
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dnas = [input().strip() for _ in range(N)]
nucleotide = ['A', 'C', 'G', 'T']

result = []
total = 0

for j in range(M):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(N):
        count[dnas[i][j]] += 1
    best_nucleotide = nucleotide[0]
    best_count = count[best_nucleotide]
    for nuc in nucleotide[1:]:
        if count[nuc] > best_count:
            best_nucleotide = nuc
            best_count = count[nuc]
    result.append(best_nucleotide)
    total += N - best_count

for res in result:
    print(res, end='')
print()
print(total)