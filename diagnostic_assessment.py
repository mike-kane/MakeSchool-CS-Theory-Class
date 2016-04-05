# Mike Kane

# 1)  Resizable Arrays



# 2)  Implement A Queue
'''
Resizable Array: NO
Not a good choice because it violates the basic principles of a queue (you should only have read access for the head,
and write access for the tail).  Semantics aside, this is also a bad choice because of the cost of inserting a node at
the tail will cost O(n) in instances where the array needs to be resized.

Circular Buffer: NO
This is not a good choice because the buffer makes it impossible to identify the head and the tail.


Singly-Linked List:  YES
This would be a good choice for a queue.  Tracking the head and the tail means that popping from the front of the queue
and adding to the end of the queue are both O(1) operations.  The user also does not have access to the the internals of
queue, which is a requirement of this data structure.

The only issue with the implementation of the SLL presented in the question is the inclusion of the 'prepend' method.
All new information added to queues goes to the back of the line--allowing the user to add data that 'skips' to the
front of the line would mean that this is no longer a queue.

'''


# 3)  Hash Table Buckets

'''
It depends on the use case of the particular hash table.  The other alternative is to only allow one item per hash value,
but make the array resizable. When a collision is detected, the hash table can iterate to the next open space, and insert
the value.  When the hash table hits a certain threshold (e.g., 60 percent full), the array can resize.  This ensures that
reading and writing data will be O(1).  Although there will be certain instances where the hash table must take the time
to resize, the amortized cost of the getting/setting data will still be O(1).  The downside to this approach is the space
cost; there will always be a minimum amount of wasted memory sitting unused(the exact amount depends on what 'tipping point
is set to cause the array to resize').

Using the linked list approach is slower, since finding data in the linked list is O(n).  However, this approach uses
memory more effectively.  If time is the most important factor, use the resizable hash table approach.  If space is most
important, use linked lists to deal with collisions.
'''


######Programming Challenges######

def fixDishes(stack):
    '''pops dishes from stack, storing them in an array.
        When stack is empty, switches positions of array[-1] and array[-2]
        reverses array and returns dishes.  '''
    dishes = []
    while stack.size != 0:
        dishes.append(stack.pop())
    dishes[-1], dishes[-2] = dishes[-2], dishes[-1]
    for dish in reversed(dishes):
        stack.push(dish)
    return stack

def makeChange()
