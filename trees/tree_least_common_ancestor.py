class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def least_common_ancestor(root, key1, key2):
    if root == None:
        return None

    if root.key == key1 or root.key == key2:
        return root

    left_lca = least_common_ancestor(root.left, key1, key2)
    right_lca = least_common_ancestor(root.right, key1, key2)

    if left_lca != None and right_lca != None:
        return root
    if left_lca == None:
        return right_lca
    else:
        return left_lca

root = Node(1, Node(2, Node(3)), Node(4, Node(5, Node(10)), Node(6)))
print least_common_ancestor(root, 6, 4).key
print least_common_ancestor(root, 2, 6).key
print least_common_ancestor(root, 10, 6).key