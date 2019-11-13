import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # counter to keep track of the number of elements in our queue
        self.size = 0
        # we'll use our LinkedList implementation to build the queue
        self.storage = DoublyLinkedList()

    def enqueue(self, item):
        # add the item to the linked list 
        self.storage.add_to_tail(item)
        # increment our size counter
        self.size += 1

    def dequeue(self):
        if self.len() > 0:
            val = self.storage.remove_from_head()
            self.size -= 1
            return val
        else:
            return None
        # remove the head of the linked list and 

    def len(self):
        return self.size