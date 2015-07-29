class Patron(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        contents = ''
        for items in self.items:
            contents += str(items) + "\n"
        return "Currently checked out items: \n" + contents


class Library(object):

    def __init__(self):
        self.shelves = []

    def __str__(self):
        contents = ''
        for books in self.shelves:
            contents += str(books)
        return contents

    def add_shelf(self, shelf):
        """add shelf object to library"""
        self.shelves.append(shelf)

    def shelf_book(self, shelf, book):
        """add a book to an existing shelf"""
        shelf.books.append(book)

    def shelf_count(self):
        """Number of shelves in Library"""
        return len(self.shelves)

    def check_out_book(self, patron, book):
        """move book object to patron, change status of book to checked out.
            """
        try:
            if book.available:
                patron.items.append(book)
                book.available = False
            else:
                print("That book is currently checked out")
        except:
            print("That book is not in our library.")

    def remove_book(self, shelf, book):
        """remove book from library"""
        shelf.books.remove(book)

    def return_book(self, patron, book):
        patron.items.remove(book)
        book.available = True


class Shelf(object):
    """create  a shelf in library for books"""

    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        contents = ''
        for book in self.books:
            contents += str(book) + "\n"
        return "The " + self.name + " shelf contains: \n" + contents


class Book(object):
    """Create a book object"""
    def __init__(self, title, author):
        """attributes: title author and availability to be checked out"""
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return self.title + ' by ' + self.author


if __name__ == '__main__':
    broadview = Library()
    f = Shelf('Fantasy')
    n = Book('The Name of The Wind', 'Patrick Rothfuss')
    broadview.add_shelf(f)
    broadview.shelf_book(f, n)
    d = Book('Dresden Files', 'Jim Butcher')
    broadview.shelf_book(f, d)
    m = Shelf('Mystery')
    broadview.add_shelf(m)
    s = Book('Sherlock Holmes', 'Arthur Conan Doyle')
    broadview.shelf_book(m, s)
    you = Patron()
    broadview.check_out_book(you, d)

    me = Patron()
    broadview.check_out_book(me, n)
