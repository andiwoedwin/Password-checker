import unittest
from accounts import Accounts

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account_credential = Accounts("Andiwo",'Edwin','AndiwoEdwin','kichwa19')
    def test_init(self):
        self.assertEqual(self.account_credential.first_name,'Andiwo')
        self.assertEqual(self.account_credential.last_name,'Edwin')
        self.assertEqual(self.account_credential.user_name,'AndiwoEdwin')
        self.assertEqual(self.account_credential.password,'kichwa19')

if __name__ == "__main__":
    unittest.main()
       
        
