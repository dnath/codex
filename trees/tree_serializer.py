class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

NONE_MARKER = '-1'
SEPARATOR = ','

def __serialize(root, char_array):
    if root == None:
        char_array.append(NONE_MARKER)
    else:
        char_array.append(str(root.key))
        __serialize(root.left, char_array)
        __serialize(root.right, char_array)


def serialize(root):
    char_array = []
    __serialize(root, char_array)
    return SEPARATOR.join(char_array)

def __deserialize(char_array):
    key = char_array.pop(0)
    if key == NONE_MARKER:
        return None
    else:
        node = Node(key)
        node.left = __deserialize(char_array)
        node.right = __deserialize(char_array)
        return node

def deserialize(tree_string):
    char_array = tree_string.split(SEPARATOR)
    root = __deserialize(char_array)
    return root

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print root.key,
    inorder(root.right)

if __name__ == '__main__':
    root = Node(1, Node(2, Node(3)), Node(4, Node(5, Node(10)), Node(6)))
    inorder(root)
    print
    tree_string = serialize(root)
    print tree_string
    root = deserialize(tree_string)
    inorder(root)
    print
    tree_string = serialize(root)
    print tree_string
