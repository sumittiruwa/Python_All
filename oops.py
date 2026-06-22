from abc import ABC, abstractmethod
import json
import os

class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass

class Person(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def role(self):
        pass

class Member(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed = []

    def role(self):
        return "Member"

class Librarian(Person):
    def role(self):
        return "Librarian"

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies <= 0:
            raise BookUnavailableError("Book unavailable")
        self.copies -= 1

    def return_book(self):
        self.copies += 1

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies
        }

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = {}
        self.load()

    def add_book(self, book):
        self.books[book.book_id] = book
        self.save()

    def remove_book(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found")
        del self.books[book_id]
        self.save()

    def search(self, keyword):
        return [
            book for book in self.books.values()
            if keyword.lower() in book.title.lower()
            or keyword.lower() in book.author.lower()
        ]

    def borrow_book(self, member, book_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found")
        book = self.books[book_id]
        book.borrow()
        member.borrowed.append(book.title)
        self.save()

    def return_book(self, member, book_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found")
        book = self.books[book_id]
        book.return_book()
        if book.title in member.borrowed:
            member.borrowed.remove(book.title)
        self.save()

    def display(self):
        if not self.books:
            print("No books available")
            return
        for book in self.books.values():
            print(
                f"{book.book_id} | {book.title} | {book.author} | Copies: {book.copies}"
            )

    def save(self):
        data = [book.to_dict() for book in self.books.values()]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename) as f:
            data = json.load(f)
            for item in data:
                self.books[item["id"]] = Book(
                    item["id"],
                    item["title"],
                    item["author"],
                    item["copies"]
                )

library = Library()
member = Member("John")

while True:
    print("\n1.Add Book")
    print("2.Remove Book")
    print("3.Display Books")
    print("4.Search")
    print("5.Borrow")
    print("6.Return")
    print("7.My Books")
    print("8.Exit")

    choice = input("Choice: ")

    try:
        if choice == "1":
            i = input("ID: ")
            t = input("Title: ")
            a = input("Author: ")
            c = int(input("Copies: "))
            library.add_book(Book(i, t, a, c))

        elif choice == "2":
            library.remove_book(input("Book ID: "))

        elif choice == "3":
            library.display()

        elif choice == "4":
            books = library.search(input("Keyword: "))
            for b in books:
                print(f"{b.book_id} | {b.title} | {b.author} | {b.copies}")

        elif choice == "5":
            library.borrow_book(member, input("Book ID: "))

        elif choice == "6":
            library.return_book(member, input("Book ID: "))

        elif choice == "7":
            if member.borrowed:
                for b in member.borrowed:
                    print(b)
            else:
                print("No borrowed books")

        elif choice == "8":
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print(e)