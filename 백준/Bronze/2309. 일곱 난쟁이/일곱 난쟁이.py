import sys
#리스트 입력받고
h = [int(sys.stdin.readline().strip()) for _ in range(9)]
#리스트 전체 합 구함
total_h=sum(h)

n1,n2 = 0, 0

#이중for써서 두명 뽑음
#a = 전체합 - 100  h[i]+h[j] == a이런식?
for i in range(9):
    for j in range(i+1, 9):
        if total_h - h[i] - h[j] == 100:
            n1, n2 = h[i], h[j]
            break
    if n1 and n2:
        break

result = [x for x in h if x != n1 and x != n2]
result.sort()
for h2 in result:
    print(h2)