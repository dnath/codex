class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def get_paths_with_distance(node, distance):
    paths = []
    __get_paths_with_distance(node, [], distance, paths)
    return paths

def __get_paths_with_distance(node, current_path, distance, paths):
    if node == None:
        return

    current_path.append(node.key)
    if len(current_path)-1 == distance:
        paths.append(current_path[:])
    else:
        __get_paths_with_distance(node.left, current_path[:], distance, paths)
        __get_paths_with_distance(node.right, current_path[:], distance, paths)


root = Node(1, Node(2, Node(3)), Node(4, Node(5, Node(10)), Node(6)))
print get_paths_with_distance(root, 0)
print get_paths_with_distance(root, 1)
print get_paths_with_distance(root, 2)
print get_paths_with_distance(root, 3)
print get_paths_with_distance(root, 4)
