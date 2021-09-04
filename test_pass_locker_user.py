import unittest
from pass_locker_user import User

class TestCase(unittest.TestCase):
    """Test class to define test cases"""
    def setUp(self):
        """To before each test case, check if the class has been initiated correctly"""
        self.new_user = User("TestUser", "1234567")
        
    def test_init(self):
        """Test if the user object is initialized correctly"""
        self.assertEqual(self.new_user.userName, "TestUser")
        self.assertEqual(self.new_user.password, "1234567")
        
    def test_save_user(self):
        """Test if the user is saved """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)
        
        

if __name__ == '__main__':
    unittest.main()
        