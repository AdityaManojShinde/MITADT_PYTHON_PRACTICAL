# Stack Implementation

class Stack:
    def __init__(self):
        self.stack = []
    def add(self, item):
        self.stack.append(item)
    def safe_pop(self):
        if not self.stack:
            print("\nStack is empty. Cannot pop item.")
            return None
        return self.stack.pop()
    def display(self):
        print("\nStack contents:")
        for index , item in enumerate(self.stack, start=1):
            print(f"\t{index}. {item}")

cart = Stack()
cart.add("item1")
cart.add("item2")
cart.add("item3")
cart.display()
item = cart.safe_pop()
if item:
    print(f"Removed item: {item}")
cart.display()
