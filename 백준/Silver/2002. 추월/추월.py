
#입구 하나(i)잡고 출구 순서랑 비교함
#출구차가 해당 입구차가 아니면 카운트
import sys
input = sys.stdin.readline
N = int(input().strip())

first = []
for _ in range(N):
    first.append(input().strip())
end = []
for _ in range(N):
    end.append(input().strip())

exit_car = set()
i = 0
ans = 0

for car in end:
    while i<N and first[i] in exit_car:
        i += 1
    if i < N and first[i] != car:
        ans += 1
    exit_car.add(car)

print(ans)