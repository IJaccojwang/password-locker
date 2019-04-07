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
        self.new_cred = Cred("IJacco" ,"Faceb", "IJaccojwang", "I1999")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Cred.credentials_array = []

    def test_init_cred(self):
        '''
        test_init test case to test if the cred object is initialized properly
        '''
        self.assertEqual(self.new_cred.username_login, "IJacco")
        self.assertEqual(self.new_cred.account, "Faceb")
        self.assertEqual(self.new_cred.username_cred, "IJaccojwang")
        self.assertEqual(self.new_cred.password_cred, "I1999")

    def test_save_cred(self):
        '''
        test_save_cred test case to test if the cred object is saved to credentials array
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Cred.credentials_array),1)

    def test_save_multiple_cred(self):
        '''
        test_save_multiple_cred to check if we can save multiple cred
        objects to our credentials_array
        '''
        self.new_cred.save_cred()
        test_cred = Cred("TC", "CredTest", "Tcred", "CT1999")
        test_cred.save_cred()
        self.assertEqual(len(Cred.credentials_array), 2)

    def test_delete_cred(self):
        '''
        test_delete_cred to test if we can remove a credential from our credentials array
        '''
        self.new_cred.save_cred()
        test_cred = Cred("TC", "CredTest", "Tcred", "CT1999")
        test_cred.save_cred()

        self.new_cred.delete_cred()
        self.assertEqual(len(Cred.credentials_array), 1)


    def test_find_cred_by_account(self):
        '''
        test to check if we can find credentials by account and display information
        '''

        self.new_cred.save_cred()
        test_cred = Cred("TC", "CredTest", "Tcred", "CT1999")
        test_cred.save_cred()
        found_cred = Cred.find_by_account("CredTest")
        self.assertEqual(found_cred.account,test_cred.account)

    def test_cred_test(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials
        '''
        self.new_cred.save_cred()
        test_cred = Cred("TC", "CredTest", "Tcred", "CT1999")
        test_cred.save_cred()
        cred_exists = Cred.cred_exist("CredTest")
        self.assertTrue(cred_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a array of all users saved
        '''
        self.assertEqual(Cred.display_creds(), Cred.credentials_array)

if __name__ == '__main__':
    unittest.main()
