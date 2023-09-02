def main():
    class Node:
        def __init__(self, key):
            self.key = key
            self.right = None
            self.left = None

    def insert(root, k):
        if root is None:
            root = Node(k)
        elif k > root.key:
            root.right = insert(root.right, k)
        else:
            root.left = insert(root.left, k)
        return root

    def inorder(root):
        if root is not None:
            inorder(root.left)
            print(str(root.key) + "-->", end=' ')
            inorder(root.right)

    def height(root):
        if root is None:
            return 0
        height_left = height(root.left)
        height_right = height(root.right)
        max_height = height_left
        if height_right > max_height:
            max_height = height_right
        return max_height + 1

    def search(root, x):
        if root is None:
            return ("The BST is empty or the node do not exist")
        if x == root.key:
            return 1
        elif x > root.key:
            return search(root.right, x)
        else:
            return search(root.left, x)

    def MinValueMax(root):
        current = root

        while current is None:
            current = current.left

        return current

    def maxValueNode(root):
        current = root

        while current.right is None:
            current = current.right

        return current.key

    def delete(root, y):
        if root is None:
            raise KeyError("The BST is empty")

        if y > root.key:
            root.right = delete(root.right, y)
        elif y < root.key:
            root.left = delete(root.left, y)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = temp

            temp = MinValueMax(root.right)

            root.key = temp

            root.right = delete(root.right, temp)

        return root

    var = input()
    var = var.split(' ')

    new_array = []
    array = []
    while True:
        try:
            info = input()
            if info == '':
                new_array.append(array)
                array = []
            else:
                array.append(info)
        except EOFError:
            new_array.append(array)
            del (new_array[0])
            break

    caio_code = var[1]

    for i in new_array[:-1]:
        if caio_code in i:
            caio_class = i

    root = None
    for k in caio_class:
        root = insert(root, k)

    caio_friends = new_array[-1]

    cont = 0

    for j in caio_friends:
        if j in caio_class:
            cont += search(root, k)

    print(cont)


if __name__ == '__main__':
    main()
