class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is currently unavailable.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def display_details(self):
        print("Book:", self.title)
        print("Author:", self.author)

        if self.is_available:
            print("Status: Available")
        else:
            print("Status: Borrowed")


book1 = LibraryBook("Python Programming", "John Smith")

book1.display_details()

book1.borrow_book()
book1.display_details()

book1.return_book()
book1.display_details()
