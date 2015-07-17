
class Library(object):
    """create Library object"""
    biblioteca = {}

    def book_count():
        """Number of shelves in Library"""
        return len(Library.biblioteca)

    def bookTitles():
        """Titles of all books present in Library"""
        all_titles = Library.biblioteca.values()
        unpacked = [j for i in all_titles for j in i]
        return ', '.join(unpacked)


class Shelf(Library):
    """create  a shelf in library for books"""

    def __init__(self, name, books):
        self.name = name
        self.books = books
        Book(self.name, self.books)
        Library.biblioteca[self.name] = [self.books] if self.books else []

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
    S = Shelf('Fantasy', 'The Name Of the Wind')
    D = Shelf('Crap', '50 Shades of Grey')
    M = Shelf('Mystery', 'Sherlock Holmes')
    S.addBook('The Stormlight Archive')
    S.delete('The Name Of the Wind')
    print(S.delete('The Way of Kings'))
    print(S.contents())
    print(M.contents())
    print(Library.bookTitles())
    print(Library.book_count())
