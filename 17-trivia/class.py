class User:
    def __init__(self,user_id, name):
        self.user_id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.user_id} years old")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_1.say_hello()

user_2 = User("002", "Syamsul")
user_2.say_hello()

user_1.follow(user_2)

print(user_1.following)