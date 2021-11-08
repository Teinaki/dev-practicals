# Research & show an example of the implementation of a circular queue. Your 
# implementation should prevent overwriting of data. Please comment your 
# code as appropriate. It helps us understand your implementation.
from collections import deque

class CircularQueue:

    #Constructor
    def __init__(self, maxSize):
        self._queue = deque([])
        self._front = 0
        self._rear = 0
        self._maxSize = maxSize

    #Adding elements to the queue
    def enqueue(self,item):
        if self.size() != self._maxSize-1:
            #if queue isn't full add the item to it
            self._queue.append(item)
            #calculate the new rear of the queue
            self._rear = (self._rear + 1) % self._maxSize
        else:
            print("Queue Full")

    #Removing elements from the queue
    def dequeue(self):
        if self.empty():
            return ("Queue Empty!") 
        data = self._queue[self._front]
        self._front = (self._front + 1) % self._maxSize
        return data

    #Calculating the size of the queue
    def size(self):
        if self._rear >= self._front:
            return (self._rear-self._front)
        return (self._maxSize - (self._front-self._rear))

    def peek(self):
        if self.empty():
            return ("Queue Empty!")
        return self._queue[self._front]
    
    def empty(self):
        return self.size() == 0
    

def main():
    queue = CircularQueue(8)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    #full here
    queue.enqueue(8)
    queue.enqueue(9)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    #empty here
    print(queue.dequeue())


if __name__ == '__main__':
    main()