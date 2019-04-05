import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("Ian", "Jaccojwang", "IJaccojwang", "I1999")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_array = []

if __name__ == '__main__':
    unittest.main()
