def preorder_traversal(node, tree):
    if node != '.':
        print(node, end="")
        preorder_traversal(tree[node][0], tree)
        preorder_traversal(tree[node][1], tree)

def inorder_traversal(node, tree):
    if node != '.':
        inorder_traversal(tree[node][0], tree)
        print(node, end="")
        inorder_traversal(tree[node][1], tree)

def postorder_traversal(node, tree):    
    if node != '.':
        postorder_traversal(tree[node][0],tree)
        postorder_traversal(tree[node][1],tree)
        print(node, end="")


N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder_traversal('A', tree)
print()
inorder_traversal('A', tree)
print()
postorder_traversal('A', tree)