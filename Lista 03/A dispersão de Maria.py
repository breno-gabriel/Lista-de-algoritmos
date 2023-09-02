class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:

    def insert(self, root, key):

        if root is None:
            return Node(key)
        elif key > root.value:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        root.height = 1 + max(self.GetHeight(root.left), self.GetHeight(root.right))

        balance = self.GetBalance(root)

        if balance > 1 and key < root.left.value:
            return self.RotateRight(root)

        if balance < -1 and key > root.right.value:
            return self.RotateLeft(root)

        if balance > 1 and key > root.left.value:
            root.left = self.RotateLeft(root.left)
            return self.RotateRight(root)

        if balance < -1 and key < root.right.value:
            root.right = self.RotateRight(root.right)
            return self.RotateLeft(root)

        return root

    def GetHeight(self, root):
        if root is None:
            return 0
        return root.height

    def RotateLeft(self, node):
        node_right = node.right
        node_right_left = node_right.left

        node_right.left = node
        node.right = node_right_left

        node.height = 1 + max(self.GetHeight(node.left), self.GetHeight(node.right))
        node_right.height = 1 + max(self.GetHeight(node_right.left), self.GetHeight(node_right.right))

        return node_right

    def RotateRight(self, node):
        node_left = node.left
        node_left_right = node_left.right

        node_left.right = node
        node.left = node_left_right

        node.height = 1 + max(self.GetHeight(node.left), self.GetHeight(node.right))
        node_left.height = 1 + max(self.GetHeight(node_left.left), self.GetHeight(node_left.right))

        return node_left

    def GetBalance(self, root):
        if root is None:
            return 0
        return self.GetHeight(root.left) - self.GetHeight(root.right)

    def preOrder(self, root):
        if root is None:
            return
        print(" {0}".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(" {0}".format(root.value), end="")
        self.inOrder(root.right)

    def posOrder(self, root):
        if root is None:
            return
        self.posOrder(root.left)
        self.posOrder(root.right)
        print(" {0}".format(root.value), end="")


def main():
    tree = AVLTree()
    root = None

    while True:
        try:
            num = int(input())
            root = tree.insert(root, num)
        except:
            break

    print("preOrdem:", end="")
    tree.preOrder(root)
    print()
    print("inOrdem:", end="")
    tree.inOrder(root)
    print()
    print("posOrdem:", end="")
    tree.posOrder(root)
    print()


if __name__ == '__main__':
    main()
