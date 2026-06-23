# Program: Queue Implementation in Python
# Type: Linear Data Structure, FIFO principle
# Operations: enqueue, dequeue, front, is_empty, size

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add item to rear of queue - O(1)"""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return front item - O(1) with deque, O(n) with list"""
        if self.is_empty():
            return "Queue Underflow - Empty"
        return self.queue.pop(0) # pop(0) is O(n) - shifts all elements

    def front(self):
        """Return front item without removing - O(1)"""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def rear(self):
        """Return rear item without removing - O(1)"""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[-1]

    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self.queue) == 0

    def size(self):
        """Return number of items - O(1)"""
        return len(self.queue)

    def display(self):
        """Print queue from front to rear"""
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f"Queue front->rear: {self.queue}")


  q = Queue()

  q.enqueue(10)
  q.enqueue(20)
  q.enqueue(30)
  q.display()

  print(f"Dequeued: {q.dequeue()}")
  print(f"Front element: {q.front()}")
  print(f"Rear element: {q.rear()}")
  print(f"Queue size: {q.size()}")
  q.display()
