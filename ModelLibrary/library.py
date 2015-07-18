
class Library:
    """create Library object"""
    biblioteca = {}

    def bookCount(self):
        """Number of shelves in Library"""
        return len(self.biblioteca)

    def bookTitles(self):
        """Titles of all books present in Library"""
        all_titles = self.biblioteca.values()
        unpacked = [j for i in all_titles for j in i]
        return ', '.join(unpacked)


class Shelf(Library):
    """create  a shelf in library for books"""

    def __init__(self, name):
        self.name = name
        Library.biblioteca[self.name] = []

    def contents(self):
        """return all titles on a specified shelf """
        shelf_contents = Library.biblioteca[self.name]
        return ', '.join(shelf_contents)

    def addBook(self, newtitle):
        """Add a book to a specific shelf, and create book object"""
        Book(newtitle)
        Library.biblioteca[self.name].append(newtitle)

    def delete(self, title):
        """If a specified book exists, delete it"""
        shelf_items = Library.biblioteca[self.name]
        try:
            shelf_items.remove(title)
        except ValueError:
            return 'That book is not on this shelf.'


class Book(Library):
    """add a book, associate with shelf in library"""
    def __init__(self, title):
        self.title = title


if __name__ == '__main__':
    broadview = Library()

    F = Shelf('Fantasy')
    F.addBook('The Dresden Files')
    F.addBook('The Name Of the Wind')

    G = Shelf('Garbage')
    G.addBook('50 Shades of Grey')

    M = Shelf('Mystery')
    M.addBook('Sherlock Holmes')

    amt = broadview.bookCount()
    print("This library currently has {} shelves.\n".format(amt))

    total = broadview.bookTitles()
    print("The titles currently in the library: {}\n".format(total))

    fan = F.contents()
    print("The Fantasy shelf currently holds: {}\n".format(fan))

    F.addBook('The Stormlight Archive')
    fan = F.contents()
    print("After adding a book, 'Fantasy' now has: {}\n".format(fan))

    F.delete('The Name Of the Wind')
    fan = F.contents()
    print("After deleting a book, 'Fantasy' now has: {}\n".format(fan))
