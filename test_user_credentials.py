
import unittest
from user_credentials import Credentials
import pyperclip

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
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Instagram", "Fidel12345")
        new_test_credential.save_credentials()
        
        credential_found = Credentials.find_account_by_name("Instagram")
        
        self.assertEqual(credential_found.account_name, new_test_credential.account_name)
        
        
    def test_credentials_exists(self):
        """
        test it we can return a boolean if the credentials already exist
        """
        self.new_credentials.save_credentials()
        test_credential =Credentials("Spotify", "123456789")
        test_credential.save_credentials()
        
        credential_exist = Credentials.credentials_exist("Spotify")
        
        self.assertTrue(credential_exist)
        
    def test_display_credentials(self):
        """test that we return all the contacts saved"""
        
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
        
    def test_copy_credential(self):
        """Test to confirm if credential have been copied"""
        
        self.new_credentials.save_credentials()
        Credentials.copy_credentials("Twitter")
        str1 = " "
      
            
            
        self.assertEqual(self.new_credentials, (str1.join(pyperclip.paste())))   
        
        
        
if __name__ == '__main__':
    unittest.main()