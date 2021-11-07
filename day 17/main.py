class User:

    def __init__(self, user_id, username):
        print("user created")
        self.id = user_id
        self.username = username


user1 = User("001", "Javier")
print(user1.id, user1.username)
