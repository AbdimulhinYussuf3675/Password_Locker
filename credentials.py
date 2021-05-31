from user import User
import pyperclip

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
        '''
        delete_credential deletes a saved credentials from credential_list
        '''
        Credentials.credential_list.remove(self) 

    @classmethod
    def check_user(cls,user_name,password):
        '''
        checks if the name and password entered exist in the users_list
        '''
        current_user = ''
        for user in User.user_list:
        	if (user.user_name == user_name and user.password == password):
        		current_user = user.user_name
        return current_user

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        method that takes in a acount_name and returns a credential that account_name
        Args:
            account_name: phone_account_name to search for
        returns:
        Credentials of person that matches the account_name 
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exist(cls, account_name):
        '''
        method that checks if a credential exists from the credential list.
        Args:
            account_name: account_name to search if it exists
        return:
            boolean: True or false depending if the credentials exist
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

            return False


    @classmethod
    def display_credentials(cls):
        '''
        method to display the list of credentials saved.
        '''
        return cls.credential_list

    @classmethod 
    def copy_credentials(cls, account_name):
        credential_found = Credentials.find_by_account_name(account_name)
        pyperclip.copy(credential_found.account_name)




    
    

