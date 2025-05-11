from collections import deque

class Queue:
    def __init__(self):
        """Initialize an empty queue using deque"""
        self.queue = deque()
        
    def enqueue(self, item):
        """Add an item to the back of the queue"""
        self.queue.append(item)
        
    def safe_dequeue(self):
        """
        Remove and return the front element from the queue
        If queue is empty, print a message and return None
        """
        if not self.queue:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.queue.popleft()
    
    def display(self):
        """Display all elements in the queue"""
        if not self.queue:
            print("\nQueue is empty.")
        else:
            print("\nQueue contents:")
            for index, item in enumerate(self.queue, start=1):
                print(f"\t{index}. {item}")
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0
    
    def size(self):
        """Return the number of elements in the queue"""
        return len(self.queue)


def main():
    # Create a new queue
    appointment_queue = Queue()
    
    # Add some patients to the queue
    print("Adding patients to the queue...")
    appointment_queue.enqueue("Patient A")
    appointment_queue.enqueue("Patient B")
    appointment_queue.enqueue("Patient C")
    
    # Display the current queue
    appointment_queue.display()
    
    # Demonstrate dequeue operation
    print("\nDequeuing patients one by one:")
    
    patient = appointment_queue.safe_dequeue()
    if patient:
        print(f"Now serving: {patient}")
    appointment_queue.display()
    
    patient = appointment_queue.safe_dequeue()
    if patient:
        print(f"Now serving: {patient}")
    appointment_queue.display()
    
    patient = appointment_queue.safe_dequeue()
    if patient:
        print(f"Now serving: {patient}")
    appointment_queue.display()
    
    # Try dequeuing from an empty queue
    print("\nAttempting to dequeue from empty queue:")
    appointment_queue.safe_dequeue()


if __name__ == "__main__":
    main()