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

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_insert_at_head(self):
        self.dll.insertAtHead(1)
        self.dll.insertAtHead(0) # 0, 1
        self.assertEqual(0, self.dll.head.data)
        self.assertEqual(1, self.dll.tail.data)

    def test_insert_at_tail(self):
        self.dll.insertAtTail(1)
        self.dll.insertAtTail(2) # 1, 2
        self.assertEqual(1, self.dll.head.data)
        self.assertEqual(2, self.dll.tail.data)

    def test_index_for_data(self):
        self.dll.insertAtTail(1)
        self.dll.insertAtTail(2)
        self.dll.insertAtTail(3)  # 1, 2, 3
        index = self.dll.getIndexForData(2)
        self.assertEqual(index, 1)

    def test_get_data_at_index(self):
        self.dll.insertAtTail(1)
        self.dll.insertAtTail(2)
        self.dll.insertAtTail(3)  # 1, 2, 3
        dataAtIndex = self.dll.getDataAtIndex(1)
        self.assertEqual(dataAtIndex, 2)

    def test_delete_data_at_index(self):
        self.dll.insertAtTail(1)
        self.dll.insertAtTail(2)
        self.dll.insertAtTail(3)      # 1, 2, 3
        self.dll.deleteNodeAtIndex(1) # 1, 3
        index = self.dll.getIndexForData(3)
        self.assertEqual(index, 1)

    def test_delete_node_with_data(self):
        self.dll.insertAtTail(1)
        self.dll.insertAtTail(2)
        self.dll.insertAtTail(3)      # 1, 2, 3
        self.dll.deleteNodeWithData(2)
        results = self.dll.getIndexForData(2)
        self.assertEqual("data not in list", results)

if __name__ == "__main__":
    unittest.main()
