class User:

    def __init__(self, user_id, username):
        print("user created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Javier")
user2 = User("002", "Angela")
print(user1.id, user1.username)

user1.follow(user2)

print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
