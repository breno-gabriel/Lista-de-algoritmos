class Heap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
            self.size = 0
        else:
            self.heap = arr[:]
            self.size = len(arr)
            for i in range(self.parent(self.size - 1), -1, -1):
                self.min_heapify(i)

    def get_size(self):
        return self.size

    def parent(self, index):
        return (index - 1) // 2

    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def min_heapify(self, index):
        smallest = index
        while True:
            l = self.leftChild(index)
            r = self.rightChild(index)
            if l < self.size and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < self.size and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def insert(self, elem):
        self.heap.append(elem)
        self.size += 1
        current = self.size - 1
        while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMin(self):
        if self.size == 0:
            return None
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.min_heapify(0)
        return popped


def main():
    while True:

        n = int(input())

        if n == 0: break

        min_heap = Heap()

        array = input().split(" ")

        for i in range(n):
            array[i] = int(array[i])
            min_heap.insert(array[i])

        custo = 0

        while min_heap.get_size() > 1:
            min1 = min_heap.extractMin()
            min2 = min_heap.extractMin()

            soma = min1 + min2

            min_heap.insert(soma)

            custo += soma

        print(custo)


if __name__ == '__main__':
    main()
