A, B = map(int,input().split())

K = A - B
if K <= 0 or K > A//2 or K > B:
    print("NO")
else:
    print("YES")
    print(K)
    #해ㅁ버거 세팅
    burger = ["aba"] * K
    #남은 재료들(ba)
    N = A-2*K
    burger[0] = burger[0] + "ba" * N
    for bugi in burger:
        print(bugi)