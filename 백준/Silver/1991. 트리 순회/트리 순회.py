import sys

input = sys.stdin.readline

n = int(input())
# 노드 개수
tree = {}

for i in range(n):
    node, l_node, r_node = input().split()
    # 전위 순회 : root - left - right
    # 중위 순회 : left - root - right
    # 후위 순회 : left - right - root
    if node not in tree:
        tree[node] = (l_node, r_node)

# 전위, 중위, 후위 순회 다 재귀함수로 어떻게 했었던 거 같은데


def preorder_traversal(node):
    if node == '.':
        return
    print(*node, end="")
    preorder_traversal(tree[node][0])
    preorder_traversal(tree[node][1])


def inorder_traversal(node):
    if node == '.':
        return
    inorder_traversal(tree[node][0])
    print(*node, end="")
    inorder_traversal(tree[node][1])


def postorder_traversal(node):
    if node == '.':
        return
    postorder_traversal(tree[node][0])
    postorder_traversal(tree[node][1])
    print(*node, end="")


preorder_traversal("A")
print()
inorder_traversal("A")
print()
postorder_traversal("A")
print()