import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x  # 작은 트리를 큰 트리에 붙임
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1  # 랭크 증가

def kruskal(V, edges):
    parent = {i: i for i in range(1, V + 1)}  # 부모 초기화
    rank = {i: 0 for i in range(1, V + 1)}  # 랭크 초기화
    edges.sort()  # 가중치 기준 정렬
    total_weight = 0  # MST 총 가중치
    count = 0  # MST 간선 개수

    for weight, a, b in edges:
        if find(parent, a) != find(parent, b):  # 사이클 발생하지 않으면 선택
            union(parent, rank, a, b)
            total_weight += weight
            count += 1

            if count == V - 1:  # MST 완성 (V-1개의 간선)
                break

    return total_weight

input = sys.stdin.readline
V, E = map(int, input().split())

edges = []
for _ in range(E):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))  # 크루스칼을 위해 (가중치, 노드1, 노드2) 형태로 저장

# 크루스칼 알고리즘 실행
print(kruskal(V, edges))
