# 거스름돈 2 or 5
# 5를 최대한 많이 쓰자
# 5로 나눠지지않으면? -> 2원을 하나 썼다고 가정하고 n -= 2 -> 개수를 count += 1 -> 5로 나눠질 때까지 반복.......

n = int(input())

count = 0
while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 2
    count += 1
else:
    print(-1)