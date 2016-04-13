sampleData = [1,2,7,5,3,0,13,509]


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self, data=None):
        self.root = None
        self.count = 0

    def add(self, data, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(data)
        if node.data == data:
            return "data already in BST!"
        if data < node.data and node.left is None:
            newNode = Node(data)
            node.left = newNode
            return "data added to BST"
        if data > node.data and node.right is None:
            newNode = Node(data)
            node.right = newNode
            return "data added to BST"

        if data < node.data:
            return add(data, node.left)
        if data > node.data:
            return add(data, node.right)

    def search(self, data):
        node = _traverse(self.root, data)
        if node is None:
            return "Data not in tree!"
        else:
            return node.data

    def _traverse(self, node, data):

        if node is None:
            return None
        elif node.data == data:
            return node

        if data < node.data:
            return _traverse(node.left, data)
        if data > node.data:
            return _traverse(node.right, data)




    def delete(self, data):
        ...
