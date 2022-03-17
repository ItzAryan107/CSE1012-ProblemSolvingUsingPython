print("QUEUE --> here is the system First in First Out")
# here the system is FIRST IN FIRST OUT(FIFO), In stack it was LIFO
queue = []
# adding element to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print("After inserting the element in Queue -->", queue)
queue.pop(0)
print(queue)
"""
it's same like stack
but what we here doing, when we popping up the element
we just popping the zeroth indexed element
just to make FIFO
else stack is also like a common list and queue is also like a common list
"""

print()

print("LINKED LIST -->")
"""
A sequential collection of data that use relation pointer
on each data node to link to the next node in the list
"""
