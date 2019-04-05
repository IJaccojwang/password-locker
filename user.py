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

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_array
        '''
        User.user_array.remove(self)

    @classmethod
    def find_by_username(cls, username_login):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username_login:  username to search for
        Returns :
            User of person that matches the username.
        '''
        for user in cls.user_array:
            if user.username_login == username_login:
                return user

    @classmethod
    def user_exist(cls, username_login):
        '''
        Method that checks if a user exists from the user array.
        Args:
            username_login:  username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_array:
            if user.username_login == username_login:
                return True

    @classmethod
    def display_users(cls):
        '''
        method that returns the user array
        '''
        return cls.user_array
