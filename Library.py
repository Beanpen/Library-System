#######################################
# Library class
#######################################
import Book as Book
import User as User

class Library:
    def __init__(self, num_book=0, num_user=0, capa=50, user=100):
        self.num_user = num_user
        self.capa = capa
        self.user = user
        self.num_book = num_book
        self.booklist = []
        self.userlist = []

    def set_num_books(self, num_book):
        self.num_book = num_book

    def get_num_books(self):
        return self.num_book

    def set_num_users(self, num_user):
        self.num_user = num_user

    def get_num_users(self):
        return self.num_user

    def set_size_books(self, capa):
        self.capa = capa

    def get_size_books(self):
        return self.capa

    def set_size_users(self, user):
        self.user = user

    def get_size_users(self):
        return self.user

    def read_books(self, fn):
        if self.num_book == self.capa:
            return -2

        opened = True
        try:
            handle = open(fn, 'r')

        except FileNotFoundError:
            opened = False
            return -1

        if opened:
            for i in handle:
                sep = i.strip().split(',')
                if sep[0] != '' and sep[1] != '':
                    sep = i.strip().split(',')
                    booktitle = sep[0]
                    bookauthor = sep[1]
                    obj = Book.Book(bookauthor, booktitle)
                    self.booklist.append(obj)
                    self.num_book += 1

                if self.num_book == self.capa:
                    return self.capa

                if i == '':
                    self.num_book += 1
                    pass

            return self.num_book

    def print_all_books(self):
        print('Here is a list of books')
        for i in self.booklist:
            print(i)

    def read_ratings(self, fn_r):
        if self.num_user >= 100:
            return -2

        opened = True
        try:
            handle = open(fn_r, 'r')

        except FileNotFoundError:
            opened = False
            return -1

        if opened:
            for i in handle:
                sep = i.strip().split(',')
                if sep[0] != '' and sep[1] != '':
                    username = sep[0]
                    rating = 0
                    ratings = []
                    for r in range(1, 51):
                        if int(sep[r]) > 0 and int(sep[r]) <= 5:
                            rating += 1
                        ratings += sep[r]
                    obj = User.User(username.lower(), ratings, rating)
                    self.userlist.append(obj)
                    self.num_user += 1

                if self.num_user == self.user:
                    return self.user

                if i == '':
                    self.num_user += 1
                    pass

            return self.num_user

    def get_rating(self, username, booktitle):
        username = username.lower()
        booktitle = booktitle.lower()
        idx_book = -1
        idx_user = -1

        for i in range(len(self.booklist)):
            if self.booklist[i].get_title().lower() == booktitle:
                idx_book = i

        for j in range(len(self.userlist)):
            if self.userlist[j].get_username().lower() == username:
                idx_user = j

        if idx_book != -1 and idx_user != -1:
            return self.userlist[idx_user].get_rating_at(idx_book)
        elif idx_book == -1 or idx_user == -1:
            return -3
        elif idx_user == -1 and idx_user == -1:
            return 1

    def get_count_read_books(self, username):
        for i in range(len(self.userlist)):
            if username.lower() == self.userlist[i].get_username():
                return self.userlist[i].get_num_ratings()
        return -3

    def view_ratings(self, username):
        n = 0
        for i in range(len(self.userlist)):
            if username.lower() == self.userlist[i].get_username():
                if int(self.userlist[i].get_num_ratings()) != 0:
                    if n == 0:
                        print('Here are the books that ' + username + ' rated:')
                        n += 1
                    for j in range(len(self.userlist[i].get_ratings())):
                        if int(self.userlist[i].get_ratings()[j]) > 0 and int(self.userlist[i].get_ratings()[j]) <= 5:
                            print('Title:', self.booklist[j].get_title(), '\nRating:',
                                  self.userlist[i].get_ratings()[j], end='\n------\n')
                    return True
                else:
                    print(username + ' has not rated any books yet.')
                    return True
        print(username + ' does not exist.')

    def calc_avg_rating(self, bookname):
        bookname = bookname.lower()
        global sum
        sum = 0
        global n
        n = 0

        for i in range(len(self.booklist)):
            if bookname == self.booklist[i].get_title().lower():
                for j in range(len(self.userlist)):
                    if int(self.userlist[j].get_ratings()[i]) > 0 and int(self.userlist[j].get_ratings()[i]) <= 5:
                        sum += int(self.userlist[j].get_ratings()[i])
                        n += 1
                try:
                    return sum / n
                except:
                    return 0
        return -3

    def add_user(self, name):
        name = name.lower()
        if self.user == self.num_user:
            return -2
        else:
            for i in range(len(self.userlist)):
                if name == self.userlist[i].get_username():
                    return 0
            new = User.User(name)
            self.userlist.append(new)
            self.num_user += 1
            return 1

    def check_out_book(self, username, booktitle, rating):
        global my_lib
        my_lib = False
        global b
        b = False
        global book_idx
        book_idx = 0
        global user_idx
        user_idx = 0

        if int(rating) not in [1, 2, 3, 4, 5]:
            return -4

        for i in range(len(self.userlist)):
            if self.userlist[i].get_username() == username.lower():
                user_idx = i
                my_lib = True

        for j in range(len(self.booklist)):
            if self.booklist[j].get_title().lower() == booktitle.lower():
                book_idx = j
                b = True

        if my_lib and b:
            self.userlist[user_idx].set_rating_at(book_idx, rating)
            return 1
        else:
            return -3