from user_credentials import Credentials
from pass_locker_user import User
import random

def create_new_credential(account_name, account_password):
    """Create a new user"""
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    "save newly created credentials"
    credentials.save_credentials()
    
def find_credential(account_name):
    """find credentials based the name account"""
    return Credentials.find_account_by_name(account_name)

def check_existing_credentials(account_name):
    """check of given account already exists"""
    return Credentials.find_account_by_name(account_name)

def display_credentials():
    "Display all the saved credentials"
    return Credentials.display_credentials()

def delete_credential(credentials):
    """Method that deletes credential"""
    return Credentials.delete_credential(credentials)

def account_options():
    while True:
        print("1: View Your Saved credentials")
        print("2: Add new credentials")
        print("3: Remove credentials")
        print("4: Search credentials")
        print("5: Log Out")
        
        selected_option = input()
        
        if selected_option == '1':
            while  True:
                print("=== List of all your credentials ===")
                if display_credentials():
                    for credential in display_credentials():
                        print(f"Account Name: {credential.account_name} | Password: {credential.account_password}")
                
                else:
                    print('\n')
                    print("You don't seem to have any credentials")
                    print('\n')
                    
                print("Return to Main Menu? y/n")
                back_to_menu = input().lower()
                if back_to_menu == 'y':
                    break
                elif back_to_menu == 'n':
                    continue
                else:
                    print("Please Enter a valid code")
                    continue
                
        elif selected_option == '2':
            




def main():
    while True:
        print("= "*20)
        
        print("  | Welcome to PassWord Locker App |\n")
        print("Use the following short codes to select an option: \n")
        short_codes = ["cu --> Create User","lg --> Login","ex --> exit Password Locker"]
        for short_code in short_codes:
            print(f"  {short_code}")
        
        print('\n')    
        short_code = input("Enter short code: ").lower()
        print('\n')
        
        if short_code == 'cu':
            print("<<=== Create a User ====>>")
            print("Create a Username")
            created_user_name = input()
            
            print("Set a Password ")
            created_user_password = input()
            
            print("Confirm your Password ")
            confirm_password = input()
            
            while confirm_password != created_user_password:
                print("Sorry your passwords did not match!!!")
                print("Set a password")
                created_user_password = input()
                print("Confirm your Password")
                confirm_password = input()
                
            else:
                print(f"Congratulations {created_user_name}! you have created your new account\n")
                print("Proceed to Log In to your Account")
                print("Enter your Username")
                entered_username = input()
                print("Enter Your Password")
                entered_password =input()
                
                while entered_username != created_user_name or entered_password != created_user_password:
                    print("You etered a wrog username or password !!")
                    print("Enter username ")
                    entered_username = input()
                    print("Enter your Password")
                    entered_password = input()
                    
                else:
                    print(f"Welcome {entered_username} to your Account\n")
                    print("Select an option below to continue: 1, 2, 3, 4, or 5")
                    
                account_options()
            
        
  
  
if __name__ == '__main__':
    main()      