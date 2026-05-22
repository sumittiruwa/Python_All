class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed:", self.name)
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print("Book returned:", self.name)


# object creation
b1 = Book("Python Basics")

b1.borrow()
b1.borrow()
b1.return_book()
b1.borrow()