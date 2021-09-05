import pyperclip

class Credentials:
    """credentials class"""
    
    def __init__(self, application_name, account_name, account_password):
        self.account_name = account_name
        self.account_password =account_password
        self.application_name =application_name
        
    """list to store credentials"""
    credentials_list = []
    
    def save_credentials(self):
        """ Method to save credentials"""
        self.credentials_list.append(self)
        
    def delete_credential(self):
        """Method to delete credential"""
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_account_by_name(cls, application_name):
        """"Method that takes account name and returns the name and password
        Args:
            account_name
        return:
           account_name and password
        """
        
        for credential in cls.credentials_list:
            if credential.application_name == application_name:
                return credential
            
    @classmethod
    def credentials_exist(cls, application_name):
        """
        Method that checks if a credential already exists
        
        Args:
            account_name: account name to search if it already exists
        Returns:
             Boolean: True or False
        """
        for credential in cls.credentials_list:
            if credential.application_name == application_name:
                return True
        return False
    
    @classmethod
    def display_credentials(cls):
        """
        method that returns credentials list
        """
        return cls.credentials_list
    
    @classmethod
    def copy_credentials(cls, application_name):
        credential_found = Credentials.find_account_by_name(application_name)
        to_copy = "Account Name: "+credential_found.account_name + " | Account Password: "+credential_found.account_password
        pyperclip.copy(to_copy)
    
