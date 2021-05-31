import unittest
from user import User
from credentials import Credentials
import pyperclip

class TestUser(unittest.TestCase):
    '''
    Test which defines test cases for the user class behaviours.
    '''
    
    
    def setUp(self):

         '''
        Set up method to run before each test cases.
        '''
        
        
        self.new_user = User('Adan', '12345')
        
    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        

        self.assertEqual(self.new_user.user_name,"Adan")
        self.assertEqual(self.new_user.password,"12345")
    
    def test_save_user(self):
         '''
        Test to check if the new users info is saved into the user list
        '''
       
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        method which cleans up after each test case has run.
        '''
        User.user_list = [] 
    
    class TestCredentials(unittest.TestCase):
        

        '''
        test class which defines test cases for the Credential class
        '''
        def setUp(self):
        '''
        setup thatrun before each test cases
        '''
        self.new_credential = Credentials('Adan','Instagram','12345')

    def test_init(self):
        '''
        test case to test weather the object is initialised properly
        '''

        self.assertEqual(self.new_credential.user_name,'Adan')
        self.assertEqual(self.new_credential.account_name,'Instagram')
        self.assertEqual(self.new_credential.password,'12345')
    
    def test_Save_credetiontials(self):
        '''
        test to check wheather new users info id saved the user list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_delete_credentials(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Khaled","Instagram","123456") # new credential
        test_credential.save_credentials()

        self.new_credential.delete_credentials()# Deleting a credential object
        self.assertEqual(len(Credentials.credential_list),2)

    def test_save_multiple_credentials(self):
        '''
        method to check if can save multiple confidential objects to confidential-list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Adan","Instagram","12345")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_account_name("Instagram")
        self.assertEqual(found_credential.account_name,test_credential.account_name)

    def test_credential_exits(self):
        '''
        test to check if we can return a Boolean if we cannot find the credential.
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Adan","Instagram","12345") # new credential
        test_credential.save_credentials()

        credential_exits =Credentials.credential_exist("Instagram")

        self.assertTrue(credential_exists)

    def test_copy_account_name(self):
        '''test to confirm that we are coping account_name from a found credential
        '''
        self.new_credential.save_credentials()
        Credentials.find_by_account_name("Instagram")

    self.assertEqual(self.new_credential.account_name,pyperclip.paste())    
    

if __name__ == '__main__':
    unittest.main()      