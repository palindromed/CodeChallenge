
class Library:
    """create Library object"""
    def __init__(self):
        self.shelves = []
        self.books = []

    def bookCount(self):
        """Number of shelves in Library"""
        return len(self.shelves)

    def bookTitles(self):
        """Titles of all books present in Library"""
        if self.books != []:
            return ', '.join(self.books)
        else:
            return 'The library is empty, add a book!'

    def createShelf(self, name):
        self.shelves.append(name)
        return Shelf(name)

    def addBook(self, title):
        self.books.append(title)
        Book(title)
        return title


class Shelf():
    """create  a shelf in library for books"""

    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return self.name

    def contents(self):
        """return all titles on a specified shelf """
        if self.books != []:
            return ', '.join(self.books)
        else:
            return 'That shelf is empty.'

    def shelveBook(self, title):
        """Add a book to a specific shelf, and create book object"""
        if title not in self.books:
            self.books.append(title)
            return self.books
        else:
            return 'That book is already on the shelf!'

    def delete(self, title):
        """If a specified book exists on the shelf, delete it"""
        try:
            self.books.remove(title)
        except ValueError:
            return 'That book is not on this shelf.'


class Book():
    """add a book, associate with shelf in library"""
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


if __name__ == '__main__':
    broadview = Library()

    Fantasy = broadview.createShelf('Fantasy')
    wind = broadview.addBook('The Name of the Wind')
    Fantasy.shelveBook(wind)
    storm = broadview.addBook('The Stormlight Archive')
    Fantasy.shelveBook(storm)
    files = broadview.addBook('The Dresden Files')
    Fantasy.shelveBook(files)

    G = broadview.createShelf('Garbage')
    Ga = broadview.addBook('50 Shades of Grey')
    G.shelveBook(Ga)

    M = broadview.createShelf('Mystery')
    mys = broadview.addBook('Sherlock Holmes')
    M.shelveBook(mys)

    amt = broadview.bookCount()
    print("This library currently has {} shelves.\n".format(amt))

    total = broadview.bookTitles()
    print("The titles currently in the library: {}\n".format(total))

    fan = Fantasy.contents()
    print("The Fantasy shelf currently holds: {}\n".format(fan))

    wheel = broadview.addBook('The Wheel of Time')
    Fantasy.shelveBook(wheel)
    fan = Fantasy.contents()
    print("After adding a book, 'Fantasy' now has: {}\n".format(fan))

    Fantasy.delete(wind)
    fan = Fantasy.contents()
    print("After deleting a book, 'Fantasy' now has: {}\n".format(fan))
