# EdX MITx.6.00.1x - Week 6

# Lecture 11 Problem 6

"""For this exercise, you will be coding your very first class, a Queue class. Queues are a fundamental computer science
data structure.

A queue is basically like a line at Disneyland - you can add elements to a queue, and they maintain a specific order.
When you want to get something off the end of a queue, you get the item that has been in there the longest
(this is known as 'first-in-first-out', or FIFO). You can read up on queues at Wikipedia if you'd like to learn more.

In your Queue class, you will need three methods:

__init__: initialize your Queue (think: how will you store the queue's elements? You'll need to initialize an appropriate object attribute in this method)
insert: inserts one element in your Queue
remove: removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError.
"""

class Queue(object):

    def __init__(self):
        """Create an empty queue"""
        self.vals = []

    def insert(self, e):
        """"Insert the value in the end of the list"""
        self.vals.append(e)

    def remove(self):
        try:
            print self.vals[0]
            del self.vals[0]
        except:
            raise ValueError



queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()

queue.insert(7)
queue.remove()

queue.remove()

queue.remove()
