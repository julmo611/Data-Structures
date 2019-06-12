class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Don't forget to wrap the value in a node
        # 1. compare the element against the current node's value
        # 2. based on the result of the comparison go  left or right
        # 3. If we find an empty spot, park the value there
        # 4. Otherwise, go back to step 1
        if value < self.value:
            # if value is less, we go left
            # if there is no left child we can park this node here
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
