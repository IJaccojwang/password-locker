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
