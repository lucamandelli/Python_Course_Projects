class User:
    def __init__(self, username, age, email, followers, following):
        self.username = username
        self.age = age
        self.email = email
        self.followers = followers
        self.following = following

    def show(self):
        show_list = [self.username, self.age, self.email, self.followers, self.following]
        print(show_list)

    def gain_followers(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("lucamandelli", "21", "luca.part.mand@gmail.com", 1550, 0)
user_2 = User("rebecafernands", "18", "rebecamello28@gmail.com", 2800, 0)
user_1.show()
user_2.show()
user_1.gain_followers(user_2)
user_2.gain_followers(user_1)
user_1.show()
user_2.show()
