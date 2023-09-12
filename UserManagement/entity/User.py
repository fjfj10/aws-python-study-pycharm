class User:

    def __init__(self, userId=None, username=None, password=None, name=None, email=None):
        self.userId = userId
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __str__(self):
        # f""할때 들여쓰기 하지말것 하면 들여쓰기 한 것까지 들어감
        return f"""[User]
userId: {self.userId}
username: {self.username}
password: {self.password}
name: {self.name}
email: {self.email}
"""