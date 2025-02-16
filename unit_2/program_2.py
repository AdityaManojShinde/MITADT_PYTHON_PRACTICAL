class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_available = True 

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"\n'{self.book_name}' by {self.author} has been checked out.")
        else:
            print(f"\nSorry, '{self.book_name}' is currently unavailable.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"\n'{self.book_name}' has been returned and is now available.")
        else:
            print(f"\n'{self.book_name}' is already available in the library.")

    def display_book(self):
        status = "Available" if self.is_available else "Checked Out"
        print(f"\nBook: {self.book_name}, Author: {self.author}, Status: {status}")


book1 = Library("Think And Grow Rich", "Nepolian Hill")
book2 = Library("Hard Things About Hard Things", "Ben Horowitz")

# Display books
book1.display_book()
book2.display_book()

# Check out a book
book1.check_out()
book1.display_book()

# Try to check out the same book again
book1.check_out()

# Return the book
book1.return_book()
book1.display_book()
