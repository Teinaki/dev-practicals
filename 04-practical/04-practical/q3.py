# Use the Stack class from question 1 and the input function 
# to reverse a string provided by a user.
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
    
    def display(self):
        """ This is not a standard stack method and is just
        included here for convenience.
        """
        print(self._stack)

def main():
    stack = Stack()

    print('Enter text to reverse: ')
    user_input = input()

    n = len(user_input)

    for i in range(0,n,1):
        stack.push(user_input[i])

    reverse = ""

    for i in range(0,n,1):
        reverse += stack.pop()

    print(reverse)


if __name__ == '__main__':
    main()