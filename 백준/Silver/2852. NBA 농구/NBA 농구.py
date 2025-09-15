import sys
input = sys.stdin.readline

n = int(input())
events = []
for _ in range(n):
    team, t = input().split()
    m, s = t.split(':')
    m = int(m)
    s = int(s)
    events.append((int(team), m*60 + s))

score1 = 0
score2 = 0
lead1 = 0
lead2 = 0
last = 0
leader = 0

for team, cur in events:
    if leader == 1:
        lead1 += cur - last
    elif leader == 2:
        lead2 += cur - last

    if team == 1:
        score1 += 1
    else:
        score2 += 1

    if score1 > score2:
        leader = 1
    elif score2 > score1:
        leader = 2
    else:
        leader = 0

    last = cur

end = 48 * 60
if leader == 1:
    lead1 += end - last
elif leader == 2:
    lead2 += end - last

m1 = lead1 // 60
s1 = lead1 % 60
mm1 = ("0" + str(m1)) if m1 < 10 else str(m1)
ss1 = ("0" + str(s1)) if s1 < 10 else str(s1)

m2 = lead2 // 60
s2 = lead2 % 60
mm2 = ("0" + str(m2)) if m2 < 10 else str(m2)
ss2 = ("0" + str(s2)) if s2 < 10 else str(s2)

print(mm1 + ":" + ss1)
print(mm2 + ":" + ss2)