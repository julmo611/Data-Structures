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
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
