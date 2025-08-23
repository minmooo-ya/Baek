import sys
input = sys.stdin.readline
N = int(input().strip())
numbers = [input().strip() for _ in range(N)]

l = len(numbers[0])

for k in range(1, l+1):
    s =set()
    for num in numbers:
        s.add(num[-k:])
    if len(s) == N:
        print(k)
        break