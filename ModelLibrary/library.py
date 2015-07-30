class Patron(object):
    def __init__(self, user):
        self.items = []
        self.user = user

    def __str__(self):
        contents = ''
        for items in self.items:
            contents += str(items) + "\n"
        return self.user + " currently has the following checked out:\n" \
            + contents


class Library(object):
    """Library class is responsible for handling shelf, book and patron
       objects.
    """

    def __init__(self):
        self.shelves = []
        self.patrons = []

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
                print(book.title + " is currently checked out. "
                      + "Try another title.\n")
        except:
            print("That book is not in our library.")

    def report_patrons(self):
        """return the patron.user value for every patron that
           belongs to this library
        """
        contents = 'This library has the following patrons: \n'
        for patron in self.patrons:
            contents += str(patron.user) + "\n"
        return contents

    def remove_book(self, shelf, book):
        """remove book from library"""
        shelf.books.remove(book)

    def return_book(self, patron, book):
        """remove book from patron and change status of book to available"""
        patron.items.remove(book)
        book.available = True

    def add_patron(self, patron):
        """add a patron to the library"""
        self.patrons.append(patron)

    def remove_patron(self, patron):
        """remove a patron from the library"""
        try:
            self.patrons.remove(patron)
        except ValueError:
            print('That patron is not in our system')


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
    # instantiate a library
    broadview = Library()
    # instantiate a shelf
    f = Shelf('Fantasy')
    # instantiate a book
    n = Book('The Name of The Wind', 'Patrick Rothfuss')
    # add shelf to library
    broadview.add_shelf(f)
    # add book to shelf in library
    broadview.shelf_book(f, n)
    # create another book
    d = Book('Dresden Files', 'Jim Butcher')
    # add to shelf already added to library
    broadview.shelf_book(f, d)
    # create another shelf
    m = Shelf('Mystery')
    # add new shelf to library
    broadview.add_shelf(m)
    # create another book
    s = Book('Sherlock Holmes', 'Arthur Conan Doyle')
    # add book to shelf
    broadview.shelf_book(m, s)
    print(broadview)
    # intantiate patrons who can check out books
    john = Patron('John')
    suzy = Patron('Suzy')

    broadview.add_patron(suzy)
    broadview.add_patron(john)
    print(broadview.report_patrons())

    # add book to patron, change flag on book to unavailable
    broadview.check_out_book(john, d)
    broadview.check_out_book(john, s)
    # show checked out items for 'john'
    print(john)
    # return a book
    broadview.return_book(john, s)
    # show book no longer in this patrons account
    print(john)
    # instantiate another patron.
    broadview.check_out_book(suzy, n)
    # if a patron tries to check out an unavailable book
    broadview.check_out_book(suzy, d)
    # show checked out items for 'suzy'
    print(suzy)
