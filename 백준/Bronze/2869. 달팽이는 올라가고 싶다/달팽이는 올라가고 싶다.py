import math

A, B, V = map(int,input().split())

m = math.ceil((V-B)/(A-B))
print(m)