A = []
for _ in range(9):
    n = int(input())
    A.append(n)

print(max(A))
print(A.index(max(A))+1)