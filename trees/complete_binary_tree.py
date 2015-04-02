class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class CompleteBinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            queue = [self.root]
            while len(queue) > 0:
                front = queue.pop(0)
                if front.left == None:
                    front.left = Node(key)
                    break
                else:
                    queue.append(front.left)

                if front.right == None:
                    front.right = Node(key)
                    break
                else:
                    queue.append(front.right)

    def __inorder(self, root):
        if root == None:
            return

        print '[',
        self.__inorder(root.left)
        print root.key,
        self.__inorder(root.right)
        print ']',

    def inorder(self):
        self.__inorder(self.root)
        print

tree = CompleteBinaryTree()
tree.insert(1)
tree.insert(2)
tree.inorder()
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.inorder()