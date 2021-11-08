# Research & show an example of the implementation of a queue using two stacks, 
# i.e., your Queue class will use two stacks to store its data. Please comment 
# your code as appropriate. It helps us understand your implementation.
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[len(self._stack)-1]
    
    def empty(self):
        return self._stack == []
          
    def size(self):
        return len(self._stack)
    
class Queue:
    def __init__(self):
        self._pushstack = Stack()
        self._popstack =Stack()

    def enqueue(self,item):
        self._pushstack.push(item)

    def dequeue(self):
        # if both the stacks are empty it will return none
        if self._pushstack.empty() and self._popstack.empty():
            return
 
        # if popstack is empty and pushstack has elements
        if self._popstack.empty() and not self._pushstack.empty():
            while not self._pushstack.empty():
                self._popstack.push(self._pushstack.pop())
                #pushes elements from the pushstack and pushes to popstack
            return self._popstack.pop()
            #then our popstack pops
            #this puts our popstack into the order we want for FIFO queue
 
        else:
            return self._popstack.pop()
            #our popstack will pop if the pushstack is empty

def main():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue('4')
    print(queue.dequeue())
    queue.enqueue('5')
    print(queue.dequeue())
    print(queue.dequeue())
    #extra dequeue to test
    print(queue.dequeue())


if __name__ == '__main__':
    main()