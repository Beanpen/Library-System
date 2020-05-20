#######################################
# Book class
#######################################
class Book:
    def __init__(self, title='', author=''):
        self.title = title
        self.author = author

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def __str__(self):
        return ('Title: ' + str(self.title) + '\nAuthor: ' + str(self.author))
