A = int(input())
B = int(input())
C = int(input())

result = A*B*C

num = list(map(int,str(result)))

for i in range(10):
    print(num.count(i))