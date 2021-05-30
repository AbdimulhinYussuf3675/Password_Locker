import unittest
from user import User

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
        method that cleans up after each test case has run.
        '''
        user_name.user_list = []


class TestCredentials(unittest.TestCase):
    '''
    test class which defines test cases for the Credential class
    '''
    def setUp(self):
        self.new_credential = Credentials('Adan','Instagram','12345')

    def test_init(self):
        '''
        test case to test weather the object is initialised properly
        '''

        self.assertEqual(self.new_credential.user_name,'Adan')
        self.assertEqual(self.new_credential.account_name,'Instagram')
        self.assertEqual(self.new_credential.password,'12345')
    
    def test_save_credentials(self)

    

if __name__ == '__main__':
    unittest.main()      