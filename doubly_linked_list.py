import unittest
'''
Doubly linked list example.  Contains methods for:
    - checking if empty
    - inserting data at head
    - inserting data at tail
    - getting index for given data
    - getting data at given index
    - deleting data at given index
    - deleting instance of data found in list

Also contains unit tests for all methods.
'''

class Node():

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        if self.head == None:
            return true
        else:
            return false

    def insertAtHead(self, data):
        ...


    def insertAtTail(self, data):
        ...

    def getIndexForData(self, data):
        ...

    def getDataAtIndex(self, index):
        ...

    def deleteNodeAtIndex(self, index):
        ...

    def deleteNodeWithData(self, data):
        ...
