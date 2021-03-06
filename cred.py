class Cred:
    """
    Class that generates new instances of credentials
    """
    credentials_array = []

    def __init__(self, username_login, account, username_cred, password_cred):
        '''
        Take input to create new credentials
        '''
        self.username_login = username_login
        self.account = account
        self.username_cred = username_cred
        self.password_cred = password_cred

    def save_cred(self):
        '''
        save_cred method saves user objects into credentials_array
        '''
        Cred.credentials_array.append(self)

    def delete_cred(self):
        '''
        delete_cred method deletes a saved credentials from the credentials_array
        '''
        Cred.credentials_array.remove(self)

    @classmethod
    def find_by_account(cls, username_login, account):
        '''
        Method that takes in an account name and returns credentials that matches that account.

        Args:
            account:  account to search for
        Returns :
            Credentials of account that matches the account name
        '''
        for cred in cls.credentials_array:
            if cred.account == account and cred.username_login == username_login:
                return cred

    @classmethod
    def cred_exist(cls, account):
        '''
        Method that checks if a credentials exists from the credentials array.
        Args:
            account:  account to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for cred in cls.credentials_array:
            if cred.account == account:
                return True

    @classmethod
    def display_creds(cls):
        '''
        method that returns the user array
        '''
        return cls.credentials_array
