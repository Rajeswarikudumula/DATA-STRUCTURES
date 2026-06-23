# Program: Stack Implementation in Python
# Type: Linear Data Structure, LIFO principle
# Operations: push, pop, peek, is_empty, size

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add item to top of stack - O(1)"""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            return "Stack Underflow - Empty"
        return self.stack.pop()

    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.stack) == 0

    def size(self):
        """Return number of items - O(1)"""
        return len(self.stack)

    def display(self):
        """Print stack from top to bottom"""
        if self.is_empty():
            print("Stack is empty")
        else:
            print(f"Stack top->bottom: {self.stack[::-1]}")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print(f"Popped: {s.pop()}")
print(f"Top element: {s.peek()}")
print(f"Stack size: {s.size()}")
s.display()
