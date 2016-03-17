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
        if self.head is None:
            return true
        else:
            return false

    def insertAtHead(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head       # set next pointer to current head
            self.head.previous = node   # set head's previous pointer to new node
            self.head = node            # assign head to new node
        self.count += 1                 # update self.count


    def insertAtTail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node       # set current tails next pointer to new node
            node.previous = self.tail   # set new nodes previous pointer to current tail
            self.tail = node            # set tail to new node
        self.count += 1                 # update self.count

    def getIndexForData(self, data):
        ''' - if list is empty, raise error saying so.
            - traverse list, keeping track of index for each node.
            - exit loop if node contains data, or if end of list is reached.
            - check which condition caused loop to break.
                - if at end of list, raise error saying data not in list.
                - if data found, return index of current node.
        '''
        if self.head is None:
            raise ValueError("list is empty!")
        index = 0
        node = self.head
        while node.data != data and node.next != None:
            node = node.next
            index += 1
        if node.data == data:
            return index
        else:
            raise ValueError("data not in list!")

    def getDataAtIndex(self, index):
        ''' - if list is empty, raise IndexError saying so
            - if index > self.count, raise IndexError error
            - traverse list, keeping track of index for each node.
            - exit list when counter == index
            - return data
        '''
        if self.head is None:
            raise ValueError("list is empty!")
        if index > self.count:
            raise IndexError("index out of range!")
        node = self.head
        count = 0
        while count != index:
            node = node.next
            count += 1
        return node.data

    def deleteNodeAtIndex(self, index):
        ''' - if list is empty, raise ValueError saying so
            - if index > self.count, raise IndexError
            - traverse list, where count == index for each node.
            - exit loop when count == index
            - get nodes that node.previous, node.next point to
            - set previous.next pointer to nextNode.
            - set nextNode.previous pointer to previous.
            - set node.previous and node.next to None.
            - decrement self.count by 1
            - return message saying node at index was successfully deleted.
        '''
        if self.head is None:
            raise ValueError("List is empty!")
        if index > self.count:
            raise IndexError("index out of range!")
        counter = 0
        node = self.head
        while counter != index:
            node = node.next
            counter += 1
        previousNode = node.previous
        nextNode = node.next
        nextNode.previous = previousNode    # backwards pointer now skips target node
        previousNode.next = nextNode        # forwards pointer now skips target node
        node.next, node.previous = None, None   # No pointers remaining, node will now be picked up by GC
        self.count -= 1
        return "node at index {} successfully deleted!".format(index)


    def deleteNodeWithData(self, data):
        ''' - If list is empty, raise ValueError saying so.
            - traverse list, checking each node to see if it contains data.
            - exit loop if data is found or end of list is reached.
            - check to see which condition forced loop to exit.
                - if data was found:
                    - get previousNode and nextNode
                    - set previous.next to nextNode
                    - set nextNode.previous to previousNode
                    - set node.next, node.previous to none.
                    -decrement self.count by 1
                    - return message informing user that first instance of data was successfully deleted.
                - if end of list was hit:
                    raise ValueError saying data was not in list!
        '''
        if self.head is None:
            raise ValueError("list is empty!")
        node = self.head
        while node.data != data and node.next != None:
            node = node.next
        if node.data == data:
            previousNode = node.previous
            nextNode = node.next
            previousNode.next = nextNode
            nextNode.previous = previousNode
            node.next, node.previous = None, None
            self.count -= 1
            return "first instance of {} was successfully deleted!".format(data)
        else:
            raise ValueError("data not in list!")




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

    def test_get_index_for_data(self):
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
        self.assertEqual(index, 1)  # test that node was deleted
        self.assertEqual(self.dll.tail.previous.data, 1)
        self.assertEqual(self.dll.head.next.data, 3)  #testing pointer logic correctness

    def test_delete_node_with_data(self):
        self.dll.insertAtTail(1)
        self.dll.insertAtTail(2)
        self.dll.insertAtTail(3)      # 1, 2, 3
        self.dll.deleteNodeWithData(2)
        with self.assertRaises(ValueError) as context:
            self.dll.getIndexForData(2)
            self.assertTrue("data not in list!" in context.ValueError)


if __name__ == "__main__":
    unittest.main()
