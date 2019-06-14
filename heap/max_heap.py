class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) > 1:
            self._swap(0, len(self.storage) - 1)
            max = self.storage.pop()
            self._sift_down(0)
        elif len(self.storage) == 1:
            max = self.storage.pop()
        else:
            return False
        return max

    def get_max(self):
        if self.storage[0]:
            return self.storage[0]
        else:
            return False

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = (index - 1)//2
        if index <= 0:
            return
        elif self.storage[index] > self.storage[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _sift_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if len(self.storage) > left and self.storage[largest] < self.storage[left]:
            largest = left
        if len(self.storage) > right and self.storage[largest] < self.storage[right]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)

    def _swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
