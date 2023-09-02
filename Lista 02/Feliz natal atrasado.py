class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(str(node.key) + " ", end="")
        inorder_traversal(node.right)

def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.key:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
        return node

def delete(node, key):
    if node is None:
        return node
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        temp = min_value_node(node.right)
        node.key = temp.key
        node.right = delete(node.right, temp.key)
    return node

def main():
    root = None
    while True:
        try:
            key = int(input())
            root = insert(root, key)
            print(height(root))
        except EOFError:
            break

if __name__ == '__main__':
    main()
