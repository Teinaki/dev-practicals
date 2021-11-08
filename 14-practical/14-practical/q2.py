from collections.abc import Sequence
# Earlier in the semester we implemented Queue classes. Take your earlier 
# Queue class and add to it so that we can treat it as an immutable sequence.
# The rationale is that this will let us inspect items in the queue
# but we can only modify the queue with the typical push() and pop().
# methods. Your new Queue should implement collections.abc.Sequence.
# Include an "if __name__ == '__main__':" section demonstrating
# the sequence properties.
class Queue(Sequence):
    def __init__(self, element):
        self._queue = element

    def __len__(self):
        return len(self._queue)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._queue[key]
        elif isinstance(key, slice):
            return Queue(self._queue[key])
        else:
            raise TypeError('Sequence access requires an int or a slice')  

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        return self._queue.popleft()

    def peek(self):
        return self._queue[0]
    
    def empty(self):
        return not self._queue
    
    def length(self):
        return len(self._queue)

if __name__ == '__main__':
    q = Queue([])
    for i in range(10):
        q.enqueue(i)
    print(q[5])
    q_slice = q[3:6]
    if isinstance(q_slice, Queue):
        print('A slice of a Queue is also a Queue')
        for q in q_slice:
            print(q)
    else:
        print('Something is not right.')
    print(q_slice[1])