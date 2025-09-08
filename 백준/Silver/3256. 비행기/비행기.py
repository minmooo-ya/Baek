import sys
input = sys.stdin.readline

N = int(input().strip())    #승객수
R = [int(input()) for _ in range(N)]    #번호리스트

A=[None]*(max(R)+1) #복도 상태
m = len(A)-1    #마지막 행 번호
i = 0   #아직 입장안한 승객 인덱스
t = 0   #시간
# 각 행에 적재중인 승객이 있으면 남은 시간 -= 1 끝나면 None
# 모든 승객 탑승 완료, 복도 비어있으면 종료
# 못앉은 승객은 앞 칸 비어있으면 앞으로 한 칸, 목표에 도탇하면 5초
# 대기 남아있고 1행 비어있으면 다음 승객 입장, 목표 1이면 5초
while True:
    for r in range(1, m+1):
        x = A[r]
        if x and x[1]>0:
            x[1] -= 1
            if x[1] == 0:
                A[r] = None

    if i==N and all(a is None for a in A[1:]):
        print(t)
        break
    for r in range(m, 0, -1):
        x = A[r]
        if x and x[1] == 0 and r+1<=m and A[r+1] is None:
            A[r+1] = x
            A[r] = None
            if x[0] == r+1:
                x[1] = 5
    if i<N and A[1] is None:
        trg = R[i]
        i += 1
        A[1] = [trg, 5 if trg == 1 else 0]
    t += 1