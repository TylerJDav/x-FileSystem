class User:
    def __init__(self, userid, capacity=1000):
        self.userid = userid
        self.capacity = capacity
    
    def set_capacity(self, capacity):
        self.capacity = capacity
