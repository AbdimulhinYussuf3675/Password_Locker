import pyperclip
from user import User
from credentials import Credentials


def create_user(user_name,password):
    '''
    Function to create new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save new user account
    '''
    user.save_user()
    
def verify_user(user_name,password):
    '''
    Function that veryfies the existing user
    
    '''
    check_user = Credentials.check_user(user_name,password)
    return check_user


def create_credential(user_name,account_name,password):
    '''
    Function that creates new creadential
    '''
    new_credential = Credentials(user_name,account_name,password)
    return new_credential

def check_existing_account(account_name):
    '''
    Function that checks if ctredential exists
    '''
    return Credentials.find_by_account_name(account_name)

def generate_password(length = 10):
    '''
    Function that generates password automatically
    '''
    letters = string.ascii_lowercase
    password_generated = ''.join(random.choice(letters) for i in range(length))
    return password_generated

def save_credentials(credential):
    '''
    Function that saves new credential
    '''
    Credentials.save_credentials(credential)
    
def delete_credential(credential):
    '''
    Function that deletes a credential
    '''
    Credentials.delete_credentials(credential)
    
def find_credential(account_name):
    '''
    Function that credential by account_name and returns credential
    '''
    return Credentials.find_by_account_name(account_name)

def display_credential(credentials):
    '''
    Function that displays saved credentials
    '''
    return Credentials.display_credentials()

def copy_credentials(credentials):
    '''
    Function that displays saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print(' ')
    print('Hello! Welcome to password Locker')
    while True:
        print("--"*50)
        print('\n')
        
        print('Use these short codes: \n cte - Create an Account \n lgn - Login \n ex - Exit')
        print('\n')
        short_code = input().lower().strip()
        if short_code == 'ex':
            break 
        
        elif short_code == 'cte':
            print("-"*20)
            print('\n')
            print('Create a new account:')
            print('\n')
           
            user_name = input('Enter your User name - ')
            password = input('Enter your password - ')
            save_user(create_user(user_name, password))
            # print(" ")
            print(f'New Account Created for: {user_name} using password: {password}')
            print('\n')

        elif short_code == 'lgn':
            print("--"*50)
            print('\n')
            print('Enter your account details to login:')
            print('\n')
            user_name = input('Enter your user name - ')
            password = str(input('Enter your password - '))
            user_exists = verify_user(user_name,password)
            if user_exists == user_name:
                print('\n')
                print(f'Welcome {user_name}. Please select a short code to continue.')
                print(' ')

                while True:
                    print("--"*50)
                    print('Our short codes: \n cc-Create your Credential \n sc-Show your Credentials \n fc- Find your Credential  \n da-delete a credential   \n ex-Exit')
                    print('\n')
                    short_code = input('Please Enter a choice: ').lower()
                    print("-"*10)


                    if short_code == 'ex':
                        print(" ")
                        print(f'Thank you for using Password Lock. Goodbye {user_name}')
                        # break

                    elif short_code == 'cc':
                        print('\n')
                        print('Please Enter your new credentials:')
                        print('\n')  
                        
                        account_name = input('Please Enter your account name - ')

                        while True:
                            print('\n')
                            print("-"*20)
                            print('Please select an option for creating a password: \n ep - enter your password \n gp - generate a password \n ex - exit')
                            choice = input('Enter an option: ').lower()
                            print("-"*10)
                            
                            if choice == 'ep':
                                
                                print('\n')
                                password = input('Enter your password: ')
                                break
                            elif choice == 'gp':
                                password = generate_password()
                                break
                            elif choice == 'ex':
                                break
                            else:
                                print('Wrong option entered. Try again!')

                        save_credentials(create_credential(user_name,account_name,password))
                        print('\n')
                        print(f'Credential Created: Account Name: {account_name} - Password: {password}')
                        print('\n')    
                    elif short_code == 'fc':
                        print("Enter the account name you want to search for:")
    
                        account_name = input()
                        if check_existing_account(account_name):
                                credential = find_credential(account_name)
                                print(f"Here is the Credentials for {credential.account_name} ")
                                print('\n')
                                print(f'account Name: {credential.account_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                                print('\n')
                                print('-' * 20)
        
                        else:
                                print('\n')
                                print("That credential does not exist")
                                
                    elif short_code == 'da':
                        print('\n')
                        print("Enter the account name of the credentials you want to remove")
                        print('\n')
    
                        account_name = input('Enter the account name- ')
                        # del_credential(credential)

                        if find_credential(account_name):
                                credential = find_credential(account_name)
                                credential.delete_credentials()									
                                print("Here is a list of all deleted credentials")
                                print('\n')


                        else:
                                print('\n')
                                print("That credential does not exist")
                                print('\n')

                    elif short_code == 'shw':
                        print('\n')
                        if display_credential(user_name):
                            print('Here is a list of all your credentials')
                            print("  ")
                            for credential in display_credential(user_name):
                                print(f'account Name: {credential.account_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print('\n')
                        else:
                            print('\n')
                            print("You don't seem to have saved any credentials yet. enter cc to create one.")
                            print('\n')

                    elif short_code == 'copy':
                        print(' ')
                        account_name = input('Enter the account name for the credential password to copy: ')
                        copy_credentials(account_name)
                        print('\n')
                    else:
                        print('Wrong option entered. Try again!')

            else:
                print(' ')
                print('Wrong details entered. Try again or Create an Account!')

        else:
            print("-"*20)
            print('\n')
            print('Wrong option entered. Try again!') 

        main() 



if __name__ == '__main__':
	main()
