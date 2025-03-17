from itertools import permutations


N = int(input())  
W = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')


cities = list(range(1, N))

for perm in permutations(cities):  
    cost = 0
    valid = True
    path = (0,) + perm + (0,)  

    for i in range(N):
        if W[path[i]][path[i+1]] == 0:  # 길이 없으면 무효
            valid = False
            break
        cost += W[path[i]][path[i+1]]

     
        if cost >= min_cost:
            valid = False
            break

    if valid:
        min_cost = min(min_cost, cost)

print(min_cost)
