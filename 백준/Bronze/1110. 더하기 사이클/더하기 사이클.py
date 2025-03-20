N = int(input())
num = N
count = 0

while True:
    x = num //10
    y = num%10
    z = (x+y) %10
    num = (y*10) + z

    count += 1
    if num == N:
        break

print(count)