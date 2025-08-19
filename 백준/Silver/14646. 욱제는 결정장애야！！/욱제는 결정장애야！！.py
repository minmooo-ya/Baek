import sys
input = sys.stdin.readline
N = int(input().strip())
numbers = list(map(int, input().strip().split()))
state = {}
answer = 0

for i in numbers:
    if i in state:
        del state[i]
    else:
        state[i] = 1
        answer = max(answer, len(state))

print(answer)