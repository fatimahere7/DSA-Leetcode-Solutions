class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Enqueue operation
    def enqueue(self, item):
        self.stack1.append(item)
        print(f"{item} enqueued to queue")

    # Dequeue operation
    def dequeue(self):
        if not self.stack2:  # If stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("Queue is empty! Cannot dequeue")
            return None

        return self.stack2.pop()

    # Peek front element
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("Queue is empty!")
            return None

        return self.stack2[-1]

    # Check if queue is empty
    def isEmpty(self):
        return not self.stack1 and not self.stack2


q = QueueUsingStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Dequeued:", q.dequeue())
q.enqueue(40)
print("Dequeued:", q.dequeue())

print("Front element:", q.peek())
