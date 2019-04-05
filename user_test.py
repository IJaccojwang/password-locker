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

    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Ian")
        self.assertEqual(self.new_user.last_name, "Jaccojwang")
        self.assertEqual(self.new_user.username_login, "IJaccojwang")
        self.assertEqual(self.new_user.password_login, "I1999")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved to user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_array),1)



if __name__ == '__main__':
    unittest.main()
