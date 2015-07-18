
class Library:
    """create Library object"""
    biblioteca = {}

    def book_count(self):
        """Number of shelves in Library"""
        return len(self.biblioteca)

    def book_titles(self):
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
        shelf_contents = Library.biblioteca[self.name]
        return ', '.join(shelf_contents)

    def addBook(self, newtitle):
        Library.biblioteca[self.name].append(newtitle)

    def delete(self, title):
        shelf_items = Library.biblioteca[self.name]
        try:
            shelf_items.remove(title)
        except ValueError:
            return 'That book is not on this shelf.'


class Book(Library):
    """add a book, associate with shelf in library"""
    def __init__(self, shelf, title):
        self.title = title
        self.shelf = shelf


if __name__ == '__main__':
    broadview = Library()

    F = Shelf('Fantasy')
    F.addBook('The Dresden Files')
    F.addBook('The Name Of the Wind')

    G = Shelf('Garbage')
    G.addBook('50 Shades of Grey')

    M = Shelf('Mystery')
    M.addBook('Sherlock Holmes')

    amt = broadview.book_count()
    print("This library currently has {} shelves.\n".format(amt))

    total = Library.book_titles
    print("this library currently holds the following titles: {}".format(total))

    fan = F.contents()
    print("The 'Fantasy' shelf currently holds: {}\n".format(fan))

    F.addBook('The Stormlight Archive')
    fan = F.contents()
    print("After adding a book, 'Fantasy' now has: {}".format(fan))

    F.delete('The Name Of the Wind')
    fan = F.contents()
    print("After deleting a book, 'Fantasy' now has: {}".format(fan))

