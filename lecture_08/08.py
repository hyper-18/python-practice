class Book:
    title = "atomic habits"
    author = "james clear"
    price = 499

    def display_details(self):
        print("book title:", self.title)
        print("author:", self.author)
        print("price:", self.price)


book1 = Book()
book1.display_details()
