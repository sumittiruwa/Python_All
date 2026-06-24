class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        name = input("Enter book name: ")
        quantity = int(input("Enter quantity: "))
        self.books[name] = self.books.get(name, 0) + quantity
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nAvailable Books:")
        for book, qty in self.books.items():
            print(f"{book} : {qty}")

    def issue_book(self):
        name = input("Enter book name to issue: ")

        if name in self.books and self.books[name] > 0:
            self.books[name] -= 1
            print("Book issued successfully!")
        else:
            print("Book not available.")

    def return_book(self):
        name = input("Enter book name to return: ")

        if name in self.books:
            self.books[name] += 1
        else:
            self.books[name] = 1

        print("Book returned successfully!")

    def delete_book(self):
        name = input("Enter book name to delete: ")

        if name in self.books:
            del self.books[name]
            print("Book deleted.")
        else:
            print("Book not found.")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.delete_book()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")