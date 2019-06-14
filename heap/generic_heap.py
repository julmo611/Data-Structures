class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        while index > 0:
            parent = index(index - 1) // 2
            if self.stotage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent

    def _sift_down(self, index):
        pass
