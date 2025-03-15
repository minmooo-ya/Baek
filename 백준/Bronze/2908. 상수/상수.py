A, B = input().split()

RA = int(str(A)[::-1])
RB = int(str(B)[::-1])

if RA<RB:
    print(RB)
else:
    print(RA)