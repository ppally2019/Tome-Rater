class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return "{} is {}".format(self.name, self.email)

    def change_email(self, address):
        self.email = address
        if self.email is not address:
            print("Your email has been updated")

    def __repr__(self):
        return "Username : {name}, Email :{email}, books read {books}".format(name=self.name, email=self.email, books=self.books)

    def __eq__(self, other):
        if other. __class__ is self. __class__:
            return (other.name, other.email, other.books) == (self.name, self.email, self.books)

    def read_book(self, book, rating=None):
        self.books[book] = rating
        return self.books

    def get_average_rating(self):
        total = 0
        for book in self.books.values():
            total += book
        try:
            average = total/len(self.books)
            return average
        except ZeroDivisionError:
            print("Can't divide by zerio!")

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        if new_isbn is not self.isbn:
            print("You have updated the ISBN")

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("That is an invalid rating")

    def __eq__(self, other):
        if other.__class__ is self. __class__:
            return (other.title, other.isbn, other.ratings) == (self.title, self.isbn, self.ratings)
        return NotImplemented

    def get_average_rating(self):
        sum = 0
        for rating in self.ratings:
            sum += rating
        return sum/len(self.ratings)

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

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):

        if email not in self.users:
            print("No user with email {email}!".format(email=email))
        self.users[email].read_book(book, rating)
        book.add_rating(rating)
        if book not in self.books:
            self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        if email in self.users:
            print("That user already exists")

        self.users[email] = new_user
        if user_books != None:
            user_books = []
            for book in user_books:
                self.add_book_to_user(book,email)

    def print_catalog(self):
        catalog = []
        for book in self.books:
            catalog.append(book)
        print(catalog)

    def print_users(self):
        users = []
        for key in self.users:
            users.append(key)
        print(users)

    def most_read_book(self):
        top_book = " "
        highest_number = 0
        for book, reads in self.books.items():
            if self.books[book] > highest_number:
                highest_number = self.books[book]
                top_book = book
        return top_book

    def highest_rated_book(self):
        favorite_book = ""
        highest_rate = float()
        for book in self.books.keys():
            if book.get_average_rating() > highest_rate:
                highest_rate = book.get_average_rating()
                favorite_book = book
        return favorite_book

    def most_positive_user(self):
        most_positive = " "
        best_average = 0
        for user in self.users.values():
            if user.get_average_rating() > best_average:
                best_average = user.get_average_rating()
                most_positive = user
        return most_positive

Tome_Rater = Tome_Rater()

#Create some books:

book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:

Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:

Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:

Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:


#Tome_Rater.print_catalog()
#Tome_Rater.print_users()
#print("Most positive user:")
#print(Tome_Rater.most_positive_user())
#print("Highest rated book:")
#print(Tome_Rater.highest_rated_book())
#print("Most read book:")
#print(Tome_Rater.most_read_book())
