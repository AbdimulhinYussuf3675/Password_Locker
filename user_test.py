import unittest
from user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User("Adan","09876")
    def test_init(self):
        self.asserEqual(self.new_user.user_name,"Adan")
        self.asserEqual(self.new_user.password,"1234")


    # def test_save_(self):
    #     self.new_user.save_user()
    #     self.asserEqual(len(User.user_list),1)

        
if __name__ == '__main__':
    unittest.main()
