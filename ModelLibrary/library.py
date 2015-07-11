#The library should be aware of a number of distinct shelves.
#Each shelf should know what books it contains.
#Create methods to add and remove a book from a self.
#The library should have a method to report all books it contains.

class Library(object):
    """create Library object"""
    biblioteca = {}

    #def __init__(self):
     #   self.total_books = {}

    def book_count(total_books):
        """Number of shelves in Library"""
        return len(Library.biblioteca)

    def bookTitles():
        """Titles of all books present in Library"""


#method for title of every book it contains



class Shelf(Library):
    """create  a shelf in library for books"""

    def __init__(self, name, books=''):
        self.name = name
        self.books = books
        Library.biblioteca[self.name] = [self.books] if self.books else []

    def addBook(self, newtitle):
        Library.biblioteca[self.name].append(newtitle)

    def contents(self):
        return Library.biblioteca[self.name].values()


#method for title of every book each shelf contains

#method to remove a particular book from shelf


class Book(object):
    """add a book, associate with shelf in library"""
    def __init__(self, title):
        self.title = title


if __name__ == '__main__':
    S = Shelf('Fantasy', 'The Name Of the Wind')
    Shelf('Crap', '50 Shades of Grey')
    Shelf('Mystery')
    S.addBook('The Stormlight Archive')
    print(Library.biblioteca)
