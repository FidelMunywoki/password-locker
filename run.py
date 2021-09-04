from user_credentials import Credentials
from pass_locker_user import User

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


