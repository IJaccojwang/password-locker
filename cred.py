class Cred:
    """
    Class that generates new instances of credentials
    """
    credentials_array = []

    def __init__(self, account, username_cred, password_cred):
        '''
        Take input to create new credentials
        '''
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
