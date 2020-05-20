#######################################
# User class
#######################################
class User:
    def __init__(self, username='', ratings=[], nr=0):
        self.username = username
        self.num_ratings = nr
        self.max_size = 50
        if ratings == []:
            self.ratings = [0] * self.max_size
        else:
            self.ratings = [0] * self.max_size
            for i in range(len(ratings)):
                if i == 50:
                    break
                else:
                    self.ratings[i] = ratings[i]

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_num_ratings(self, num_ratings):
        self.num_ratings = num_ratings

    def get_num_ratings(self):
        return self.num_ratings

    def set_ratings(self, ratings):
        self.ratings = ratings

    def get_ratings(self):
        return self.ratings

    def get_rating_at(self, idx_rating):
        if idx_rating < 0 or idx_rating >= self.max_size:
            return -1
        else:
            return self.ratings[idx_rating]

    def set_rating_at(self, index_ratings, actual_num):
        if len(self.ratings) <= index_ratings:
            return False
        if actual_num <= 5 and actual_num >= 0:
            self.ratings[index_ratings] = actual_num
            return True
        else:
            return False

    def __str__(self):
        return 'Username: ' + (self.username) + '\nRated ' + str(self.num_ratings) + ' books'
