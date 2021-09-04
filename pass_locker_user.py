class User:
    """users class """

    users_list =[]
    
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        
    def save_user(self):
        """saves the user object to user list"""
        
        self.users_list.append(self)