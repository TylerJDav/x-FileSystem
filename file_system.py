from file import File
from user import User

class file_system:
    def __init__(self):
        self.total_size = 100000000
        self.file_system = []
        self.users = []
        self.admin = User("admin", self.total_size)

    def add_file(self, name, size, user=None):
        if user is None:
            user = self.admin
        if self.get_file(name) is not None:
            return False
        self.file_system.append(File(name, size, user))
        return True
    
    def add_user(self, userid, capacity=None):
        if self.get_user(userid) is not None:
            return False
        if capacity is not None:
            self.users.append(User(userid, capacity))
        else:
            self.users.append(User(userid))
        return True
    
    def get_file(self, file_name):
        for file in self.file_system:
            if file.name == file_name:
                return file
        return None
    
    def get_user(self, userid):
        for user in self.users:
            if user.userid == userid:
                return user
        return None
    
    def change_user_capacity(self, userid, capacity):
        curr_user = self.get_user(userid)
        if curr_user is None:
            return False
        curr_user.set_capacity(capacity)
        return True
    
    def copy_file(self, from_file_name, to_file_name):
        from_file = self.get_file(from_file_name)
        if from_file is None:
            return False
        to_file = self.get_file(to_file_name)
        if to_file is None:
            return False
        
        to_file = File(to_file_name, from_file.size, from_file.user)
        self.file_system.append(to_file)
        return True
    
    def find_file(self, prefix, suffix):
        output = []
        for file in self.file_system:
            if file.name[:len(prefix)] == prefix and file.name[-len(suffix):] == suffix:
                output.append(f"{file.name}({file.size})")
        output.sort()
        return sorted(output, key=lambda f: f[-3:])
    
    def add_file_by(self, name, size, userid):
        return self.add_file(name, size, userid)
    
    def delete_file(self, file_name):
        file = self.get_file(file_name)
        if file:
            self.file_system.pop(file)
            return True
        else:
            return False
    
    def delete_user(self, userid, deep=False):
        for user in self.users:
            if user.userid == userid:
                self.users.pop(user)
                
                for file in self.file_system:
                    if file.user == userid:
                        if deep:
                            self.file_system.pop(file)
                        else:
                            self.file_system[file].change_user(self.admin)

                return True
        return False
    