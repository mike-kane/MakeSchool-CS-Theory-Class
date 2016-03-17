import unittest

'''
Singly linked list example.  Contains methods for:
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
        self.next = None

class singly_linked_list():

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
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.count += 1


    def insertAtTail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1


    def getIndexForData(self, data):
        if self.head is None:
            return "list is empty!"
        counter = 0
        node = self.head
        while node.data != data and node.next != None:
            node = node.next
            counter += 1
        if node.data == data:
            return counter
        elif node.next == None:
            return "data not in list"

    def getDataAtIndex(self, index):
        ''' -  If list is empty, return error saying so
            -  Traverse list, keeping track of index for each node
            -  If counter == index or if end of list, exit loop
            -  check to see which condition made loop exit
                    - if end of list, return error saying data not in list
                    - if at index, return data attached to node
         '''
        if self.head is None:
            return "list is empty!"
        counter = 0
        node = self.head
        while counter != index and node.next != None:
            node = node.next
            counter += 1
        if counter == index:
            return node.data
        else:
            return "data not in list"

    def deleteNodeWithData(self, data):
        ''' - if list is empty, return message saying so
            - begin traversing list.  Keep track of pointers for current node and previous node
            - exit loop if current node contains target data, or if at end of List
            - check with condition caused loop to break
                - if end of list, return message saying data not in List
                - if data found:
                    - previous.next = current.next
                    - current.next = None
                    - no pointers coming from or pointing at node, will now be picked up by GC
                    - decrement self.count by 1
        '''

        if self.head is None:
            return "List is empty!"
        node = self.head
        previous = None
        while node.data != data and node.next != None:
            previous = node
            node = node.next
        if node.next == None:
            return "data not in list!"
        else:
            previous.next = node.next
            node.next = None
            self.count -= 1
            return "First instance of {} removed from list".format(data)


    def deleteNodeAtIndex(self, index):
        ''' - If list is empty, return message saying so
            - use counter variable to keep track of index as list is traversed.  Keep track of node and previousNode
            - check if index input is greater than self.count.  If so, raise IndexError
            - exit loop if counter == index
                - previous.next = node.next
                - node.next = None
                - decrement self.count by 1
                - return message letting user know that data at index has been successfully deleted.
        '''
        if self.head is None:
            return "list is empty!"
        elif index > self.count:
            raise IndexError("index out of range!")
        node = self.head
        previous = None
        counter = 0
        while counter != index:
            previous = node
            node = node.next
            counter += 1
        previous.next = node.next
        node.next = None
        self.count -= 1
        return "node at index {} successfully deleted!".format(index)




class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.sll = singly_linked_list()

    def test_insert_at_head(self):
        self.sll.insertAtHead(1)
        self.assertEqual(1, self.sll.head.data)

    def test_insert_at_tail(self):
        self.sll.insertAtTail(1)
        self.sll.insertAtTail(2)
        self.assertEqual(2, self.sll.tail.data)

    def test_get_index_for_data(self):
        self.sll.insertAtTail(1)
        self.sll.insertAtTail(2)
        self.sll.insertAtTail(3)  # 1, 2, 3
        index = self.sll.getIndexForData(2)
        self.assertEqual(index, 1)

    def test_get_data_at_index(self):
        self.sll.insertAtTail(1)
        self.sll.insertAtTail(2)
        self.sll.insertAtTail(3)  # 1, 2, 3
        dataAtIndex = self.sll.getDataAtIndex(1)
        self.assertEqual(dataAtIndex, 2)

    def test_delete_data_at_index(self):
        self.sll.insertAtTail(1)
        self.sll.insertAtTail(2)
        self.sll.insertAtTail(3)      # 1, 2, 3
        self.sll.deleteNodeAtIndex(1) # 1, 3
        index = self.sll.getIndexForData(3)
        self.assertEqual(index, 1)

    def test_delete_node_with_data(self):
        self.sll.insertAtTail(1)
        self.sll.insertAtTail(2)
        self.sll.insertAtTail(3)      # 1, 2, 3
        self.sll.deleteNodeWithData(2)
        results = self.sll.getIndexForData(2)
        self.assertEqual("data not in list", results)

if __name__ == "__main__":
    unittest.main()
