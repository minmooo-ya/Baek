N = int(input())

count = 0

for i in range(1, N+1):
    if i <= 99:
        count += 1

    else:
        han = list(map(int,str(i)))
        if han[1]-han[0] == han[2]-han[1]:
            count += 1

print(count)

#str로 나눠 연속된 두 자리수끼리 뺄셈
#같은 수 나오면 한수