class Book:
    def __init__(self, id, title, author, price):
        self.book_id = id
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self, percent):
        self.price = self.price - (self.price * percent / 100)
    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Price: {self.price}")
book = Book(2, "Best Quest", "Riley", 1000)
book.apply_discount(10)
book.display_info()