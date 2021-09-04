class Credentials:
    """credentials class"""
    
    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password =account_password
        
    """list to store credentials"""
    credentials_list = []
    
    def save_credentials(self):
        """ Method to save credentials"""
        self.credentials_list.append(self)
        
    def delete_credential(self):
        """Method to delete credential"""
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_account_by_name(cls, account_name):
        """"Method that takes account name and returns the name and password
        Args:
            account_name
        return:
           account_name and password
        """
        
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
    
