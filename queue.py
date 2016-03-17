import unittest

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Queue():

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
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def peek(self):
        if self.head is None:
            raise ValueError("list is empty!")
        else:
            return self.head.data

    def pop(self):
        if self.head is None:
            raise ValueError("list is empty!")
        else:
            dataToReturn = self.head.data
            newHead = self.head.next
            newHead.previous = None
            self.head.next = None
            self.head = newHead
            self.count -= 1
            return dataToReturn

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()


    def test_add(self):
        self.q.add(1)
        self.q.add(2)
        self.q.add(3)
        self.assertEqual(self.q.tail.data, 3)
        self.assertEqual(self.q.head.data, 1)

    def test_pop(self):
        self.q.add(1)
        self.q.add(2)
        self.q.add(3)
        expectedReturn = self.q.pop()
        self.assertEqual(expectedReturn, 1)
        expectedNewHead = self.q.peek()
        self.assertEqual(expectedNewHead, 2)

    def test_peek(self):
        self.q.add(1)
        self.q.add(2)
        self.q.add(3)
        expectedReturn = self.q.peek()
        self.assertEqual(expectedReturn, 1)

if __name__ == "__main__":
    unittest.main()
