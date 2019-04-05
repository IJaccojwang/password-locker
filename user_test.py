import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
username_login
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
        test_save_user test case to test if the user object is saved to user array
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_array),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        bjects to our user_array
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "Tuser", "T1999")
        test_user.save_user()
        self.assertEqual(len(User.user_array), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user array
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "Tuser", "T1999")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_array), 1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test", "User", "Tuser", "T1999")
        test_user.save_user()
        found_user = User.find_by_username("Tuser")
        self.assertEqual(found_user.username_login,test_user.username_login)

    def test_user_test(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "Tuser", "T1999")
        test_user.save_user()
        user_exists = User.user_exist("Tuser")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
