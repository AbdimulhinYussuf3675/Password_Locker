import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    
    
    def setUp(self):
        
        
        self.new_user = User('Adan', '12345')
        
    def test_init(self):
        

        self.assertEqual(self.new_user.user_name,"Adan")
        self.assertEqual(self.new_user.password,"12345")
    
    def test_save_user(self):
       
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
    

if __name__ == '__main__':
    unittest.main()      