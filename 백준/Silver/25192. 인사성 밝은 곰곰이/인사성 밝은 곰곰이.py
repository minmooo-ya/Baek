import sys
input = sys.stdin.readline

N = int(input().strip())
chat = set()
ans = 0

for _ in range(N):
    name = input().strip()
    if name == "ENTER":
        chat.clear()
    else:
        if name not in chat:
            ans += 1
            chat.add(name)
print(ans)