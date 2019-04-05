class User:
    """
    Class to generate new instances of users
    """
    user_array = []

    def __init__(self, first_name, last_name, username_login, password_login):
        '''
        To take user input to create a new user
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username_login = username_login
        self.password_login = password_login

    def save_user(self):
        '''
        save_user method saves user objects into user_array
        '''
        User.user_array.append(self)
