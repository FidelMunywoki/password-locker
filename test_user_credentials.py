
import unittest
from user_credentials import Credentials

class TestCredentials(unittest.TestCase):
    """Test class for Credentials behaviour"""
    
    def setUp(self):
        "method to run before each test case"
        self.new_credentials = Credentials("Twitter", "Fidel1234")
        
    def test_credentials_init(self):
        """Method to check if new_credentials have been initialized correctly"""
        self.assertEqual(self.new_credentials.account_name, "Twitter")
        self.assertEqual(self.new_credentials.account_password, "Fidel1234" )
        
    def test_save_credetials(self):
        """Method to check if new_credentials have been saved"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_save_multiple_credentials(self):
        """Method to check save multiples credentials to credentials list"""
        self.new_credentials.save_credentials()
        new_second_credentials = Credentials("Facebook", "Fidel4321")
        new_second_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def tearDown(self):
        """Method to clear credentials list after each test case"""
        Credentials.credentials_list = []
        
    def test_delete_credential(self):
        """Method to test delete credential"""
        self.new_credentials.save_credentials()
        new_second_credentials = Credentials("Facebook", "Fidel4321")
        new_second_credentials.save_credentials()
        Credentials.delete_credential(new_second_credentials)
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_account_by_name(self):
        """Test if we can find credentials"""
        
    
if __name__ == '__main__':
    unittest.main()