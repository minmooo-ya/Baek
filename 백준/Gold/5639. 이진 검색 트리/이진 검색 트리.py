import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

# 후위 순회를 위한 재귀 함수
def postorder(left, right):
    if left > right:
        return

    # 루트 노드는 tree[left]이고, 이를 기준으로 서브트리를 나눔
    mid = right + 1
    for i in range(left + 1, right + 1):
        if tree[left] < tree[i]:
            mid = i
            break

    # 왼쪽 서브트리 후위 순회
    postorder(left + 1, mid - 1)
    # 오른쪽 서브트리 후위 순회
    postorder(mid, right)
    # 현재 노드 출력
    print(tree[left])

# 후위 순회 시작
postorder(0, len(tree) - 1)
