class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

class IterableCollection:
    def create_iterator(self):
        pass

class Book:
    def __init__(self, title):
        self.title = title

class BookCollection(IterableCollection):
    def __init__(self, books):
        self.books = books

    def create_iterator(self):
        return BookIterator(self)

class BookIterator(Iterator):
    def __init__(self, book_collection):
        self.book_collection = book_collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.book_collection.books)

    def next(self):
        if self.has_next():
            book = self.book_collection.books[self.index]
            self.index += 1
            return book
        else:
            return None

class Magazine:
    def __init__(self, title):
        self.title = title

class MagazineCollection(IterableCollection):
    def __init__(self, magazines):
        self.magazines = magazines

    def create_iterator(self):
        return MagazineIterator(self)

class MagazineIterator(Iterator):
    def __init__(self, magazine_collection):
        self.magazine_collection = magazine_collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.magazine_collection.magazines)

    def next(self):
        if self.has_next():
            magazine = self.magazine_collection.magazines[self.index]
            self.index += 1
            return magazine
        else:
            return None

books = [Book("Book 1"), Book("Book 2"), Book("Book 3")]
book_collection = BookCollection(books)
book_iterator = book_collection.create_iterator()

while book_iterator.has_next():
    book = book_iterator.next()
    print(book.title)

magazines = [Magazine("Magazine 1"), Magazine("Magazine 2"), Magazine("Magazine 3")]
magazine_collection = MagazineCollection(magazines)
magazine_iterator = magazine_collection.create_iterator()

while magazine_iterator.has_next():
    magazine = magazine_iterator.next()
    print(magazine.title)
