import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
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

if __name__ == '__main__':
    unittest.main()      