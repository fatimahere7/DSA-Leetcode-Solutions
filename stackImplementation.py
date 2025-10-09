class Stack:
    def __init__(self):
        self.stack = []   # stack is implemented using a list

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    # Pop element from stack
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack Underflow! Cannot pop from empty stack")

    # Peek top element
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element:", s.peek())

s.pop()
s.display()
