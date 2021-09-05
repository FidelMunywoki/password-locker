from user_credentials import Credentials
from pass_locker_user import User
import random
import string

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

def generate_random_password(length):
  return ''.join(random.choice(string.printable) for i in range(length))

def copy_credential(account_name):
    return Credentials.copy_credentials(account_name)

def account_options():
    while True:
        print("<<<---- MAIN MENU ---->>>")
        print("1: View Your Saved credentials")
        print("2: Add new credentials")
        print("3: Remove credentials")
        print("4: Search credentials")
        print("5: Copy Credentials")
        print("6: Log Out")
        
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
            while True:
                print("Add New Credentials")
                print("Enter Account Name")
                account_name = input()
                print("Enter a password")
                
                print(" << Press 'gp' to generate a password instead !! press 'n' to continue")
                pressed_key = input().lower()
                if pressed_key == 'gp':
                    password_length = input("Enter the length of password to generate ")
                    account_password = generate_random_password(int(password_length))
                    print(f"Account Name: {account_name}")
                    print(f"Account Password: {account_password}")
                    print('\n')
                    
                elif pressed_key == 'n':
                    print('\n')
                    print("Create Your Password")
                    account_password = input()
                    print(f"Account Name: {account_name}")
                    print(f"Account Password: {account_password}")
                    
                save_new_credential(create_new_credential(account_name, account_password))
                    
                break
            
        elif selected_option ==  '3':
            while True:
                print("Search for Credential to delete")
                print("Enter account name to delete:")
                
                search_name = input()
                
                if check_existing_credentials(search_name):
                    found_credential = find_credential(search_name)
                    print("Found Credential \n")
                    print(f"Account Name: {found_credential.account_name} \n Password: {found_credential.account_password}")
                    print("Delete? y/n")
                    
                    sure = input().lower()
                    if sure == 'y':
                        delete_credential(found_credential)
                        print("Account Credentials deleted Successfully ...")
                        break
                    elif sure == 'n':
                        continue
                    
                else:
                    print("That contact does not exist")
                    break
                
        elif selected_option == '4':
            while True:
                print("Enter an account name to find credentials for: ")
                search_name = input()
                
                if check_existing_credentials(search_name):
                    found_credential = find_credential(search_name)
                    print("Found Credential \n")
                    print(f"Account Name: {found_credential.account_name} \n Password: {found_credential.account_password}")
                    print('\n')
                
                    
                else:
                    print("That contact does not exist")
                    
                break
        elif selected_option == '5':
            print("Enter the account name to copy credentials for ")
            search_name = input()
            
            if check_existing_credentials(search_name):
                    found_credential = find_credential(search_name)
                    print("Account name and password successfully copied to clipboard >> \n")
                    Credentials.copy_credentials(found_credential.account_name)
            
        elif selected_option == '6':
            print("WARNING!! You will loose all your saved credentials for now \n We are working on implementing a database soon")
            print("Are sure you want to continue? y/n")
            logout = input().lower()
            if logout == 'y':
                print("You have successfully logged out")
                break
            elif logout == 'n':
                continue
             
           
                              
                
            




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
                
        elif short_code == 'lg':
            print("Welcome to Password Locker")
            print("Enter Username:")
            default_user_name = input()
            
            print("Enter Password:")
            default_user_password = input()
            print('\n')
            
            while default_user_name != 'testuser' or default_user_password != '12345':
                print("Invalid userame or password | Username 'testuser', Password '12345' ")
                print("Enter Username:")
                default_user_name = input()
                
                print("Enter Password:")
                default_user_password = input()
                print('\n')
                
            if default_user_name == 'testuser' and default_user_password == '12345':
                print("You have successfully logged in!!...\n")
                
                print(f"Welcome {default_user_name} to your Account\n")
                print("Select an option below to continue: 1, 2, 3, 4, or 5")
                
            account_options()
            
        elif short_code == 'ex':
            break
        
            
        
        else:
            print("Please enter a valid code to continue")
                
                
            
        
  
  
if __name__ == '__main__':
    main()      