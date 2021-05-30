# import pyperclip #importing pyperclip for copying to clipboard

class User:
    '''
    class that allows user to generate user account
    '''
    
    user_list = []
    
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        
