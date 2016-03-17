import unittest


class Node():

    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data

class Stack():
    '''
        - LIFO: Last-In-First-Out
        - Peek: return data from last node added
        - Pop: return data from last node added and remove node
     '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        self.count += 1

    def peek(self):
        if self.head is None:
            raise ValueError("Stack is empty!")
        else:
            return self.tail.data

    def pop(self):
        '''
            - if list is empty, raise ValueError
            - if list is not empty, grab data from tail and store in var node
            - remove previous pointer from self.tail node
            - remove next pointer from node before self.previous node
            - set new node to tail
         '''
        if self.head is None:
            raise ValueError("Stack is empty!")
        else:
            data = self.tail.data           # get data
            newTail = self.tail.previous    # get node that will become new tail
            self.tail.previous = None
            newTail.next = None
            self.tail = newTail
            self.count -= 1
            return data

    def __str__(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_add(self):
        x = [x for x in range(3)]
        for number in x:
            self.stack.add(number)
        print(self.stack.tail.data)
        self.assertEqual(2, self.stack.tail.data)

    def test_peek(self):
        ...

    def test_pop(self):
        ...

if __name__ == "__main__":
    unittest.main()
