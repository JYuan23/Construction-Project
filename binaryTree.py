class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, data):
        if data < self.data:
            self.left = BinaryTree(data)
        else:
            self.right = BinaryTree(data)

    def print(self):
        print(self.data)


bt = BinaryTree(10)
bt.append(20)
bt.append(2)