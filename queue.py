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
        ...

    def peek(self):
        ...

    def pop(self):
        ...

class TestQueue(unittest.TestCase):

    def setUp(self):
        ...


    def test_add(self):
        ...


    def test_pop(self):
        ...
        

    def test_peek(self):
        ...
