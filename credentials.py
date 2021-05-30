from user import User

class Credentials:
    '''
    class to create account credentials.
    '''
    credential_list = []
    def __init__(self,user_name,account_name,password):
        '''
        method to define the properties
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        A method that saves new user object
        '''
        Credentials.credential_list.append(self)
    
    def delete_credentials(self):
        Credentials.credential_list.remove(self)
    
    

