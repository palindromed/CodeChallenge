#The library should be aware of a number of distinct shelves.
#Each shelf should know what books it contains.
#Create methods to add and remove a book from a self.
#The library should have a method to report all books it contains.

class Library(object):
    """create Library object"""
    d = {shelf: [books]}
    def __init__(self):
        self.total_books = {}

    def book_count(total_books):
#create a dict to keep all shelves and which books they're on.
#1 method for len of the dict(number of shelves)
#method for title of every book it contains
        #{key:value for values}a dict comp for 1 of the methods?




class Shelf(object):
    """create  a shelf in library for books"""
    def __init__(self, name):
        self.name = name
        self.books = #dict values that go along with shelf
#method for title of every book each shelf contains
#add method to add a book to an existing shelf
#method to remove a particular book from shelf




class Book(object):
    """add a book, associate with shelf in library"""
    def __init__(self, title):
        self.title = title
        self.shelf =

