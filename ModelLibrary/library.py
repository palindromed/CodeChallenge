class Patron(object):
    def __init__(self):
        self.books = []

class Library(object):

    def __init__(self):
        self.shelves = []

    def __str__(self):
        contents = ''
        for books in self.shelves:
            contents += str(books)
        return contents

    def add_shelf(self, shelf):
        """add shelf to library"""
        self.shelves.append(shelf)

    def shelf_book(self, shelf, book):
        """return a book that had been checked out or add new book"""
        shelf.books.append(book)

    def shelf_count(self):
        """Number of shelves in Library"""
        return len(self.shelves)

    def check_out_book(self, shelf, book, patron):
        """take book from library and give to patron"""
        shelf.books.pop(book)
        patron.books.append(book)



class Shelf(object):
    """create  a shelf in library for books"""

    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        contents = ''
        for book in self.books:
            contents += str(book) + "\n"
        return "The shelf " + self.name + " contains: " + contents


class Book(object):
    """add a book, associate with shelf in library"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author


if __name__ == '__main__':
    broadview = Library()
    f = Shelf('fantasy')
    n = Book('Wind', 'Rothfuss')
    broadview.add_shelf(f)
    broadview.shelf_book(f, n)
    me = Patron()
