import unittest
from cred import Cred

class Testcred(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_cred = Cred("Faceb", "IJaccojwang", "I1999")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Cred.credentials_array = []

    def test_init_cred(self):
        '''
        test_init test case to test if the cred object is initialized properly
        '''
        self.assertEqual(self.new_cred.account, "Faceb")
        self.assertEqual(self.new_cred.username_cred, "IJaccojwang")
        self.assertEqual(self.new_cred.password_cred, "I1999")


if __name__ == '__main__':
    unittest.main()
