from itertools import combinations
import sys

h = [int(sys.stdin.readline().strip()) for _ in range(9)]
new_h = []

for i in list(combinations(h,7)):
    if sum(i) == 100:
        new_h=i

new_h = list(new_h)
new_h.sort()
print("\n".join(map(str, new_h)))