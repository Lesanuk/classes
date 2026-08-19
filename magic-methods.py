
class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # string representation of the object
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other): # equality comparison
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): # less than
        return self.num_pages < other.num_pages

    def __gt__(self, other): # greater than
        return self.num_pages > other.num_pages

    def __add__(self, other): # addition
        return f"{self.num_pages + other.num_pages} pages in total"

    def __contains__(self, keyword): # membership test
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key): # get item by key
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
book2 = Book("Atomic Habits", "James Clear", 320)
book3 = Book("You can't hurt me", "David Goggins", 364)

print(book2)
print(book1 == book3)
print(book1 < book3)
print(book1 > book3)
print(book1 + book2)
print("z" in book1)
print(book1['title'])
print(book1['audio'])