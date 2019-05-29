# Tome-Rater
This is my TOME Rater stuff

class User(object):
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.books = {}

        def get_email(self):
            return "{} is {}".format(self.name, self.email)

        def change_email(self, address):
            self.email = address
            print("Your email has been updated")


        def __repr__(self):
            return "Username : {name}, Email :{email}, books read {books}".format(name=self.name, email=self.email, books=self.books)

        def __eq__(self, other):
            if self.email == other.email:
                self = other

        def read_book(self, book, rating = None):
            self.books[book] = rating

        def get_average_rating(self):
            total = 0
            for book in self.books.values():
                total += book
            return total / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return(self.isbn)

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("You have updated the ISBN")

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("That is an invalid rating")

    def __eq__(self, other):
        if other.title == self.title:
            self = other

    def get_average_rating(self):
        total = 0
        for rating in self.ratings.values():
            rating += average
        return average / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} was written by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a level {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class Tome_Rater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self,title, subject, level, isbn):
        new_nonfiction = Non_Fiction(title, subject, level, isbn)
        return new_nonfiction

    def add_book_to_user(self, book, email, rating = 0):
        key_to_check = email
        try:
            print(self.users[key_to_check])
        except KeyError:
            print("No user with the email {email} exists!".format(email=email))

        self.users[email] =







#
# def add_user(self, name, email, user_books= []):
#     User(name, email)
#     for book in user_books:
#         Tome_Rater.add_book_to_user(book, email)
#
# def print_catalog(self):
#     catalog = []
#     for book in self.books:
#         catalog.append(key)
#     print(catalog)
#
# def print_users(self):
#     users = []
#     for key in self.users:
#         users.append(key)
#     print(users)
#
# def most_read_book(self):
#     counter = 0
#     while key in self.books:
#         if self.books[book] > counter:
#             counter = key
#     return counter
#
# def highest_rated_book(self):
#     highest_average = 0
#     for book in self.books:
#         if Book.get_average_rating(book) > highest_average:
#             highest_average = book
#     return highest_average
#
# def most_positive_user(self):
#     most_positive = 0
#     while key in self.users:
#         if key.get_average_rating() > most_positive:
#             most_positive = key
#     return most_positive

Tome_Rater.create_book("Swamp Thing", 2335)
Tome_Rater.create_novel("Free Biscuits!", "Sir Willy Smith Smith", 3939)
Tome_Rater.create_non_fiction("Herb Time", "Plants", "Beginner", 39494)
