from user import User

class File:
    def __init__(self, user, name, size):
        self.user = user
        self.name = name
        self.size = size
        
    def change_user(self, userid):
        self.userid = userid
