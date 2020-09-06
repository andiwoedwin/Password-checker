import unittest
from accounts import Accounts

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account_credential = Accounts("Andiwo",'Edwin','AndiwoEdwin','kichwa19')

    def tearDown(self):
        Accounts.account_names=[]
    def test_init(self):
        self.assertEqual(self.account_credential.first_name,'Andiwo')
        self.assertEqual(self.account_credential.last_name,'Edwin')
        self.assertEqual(self.account_credential.user_name,'AndiwoEdwin')
        self.assertEqual(self.account_credential.password,'kichwa19')

    def test_save_account(self):
        self.account_credential.save_account()
        self.assertEqual(len(Accounts.account_names),1)

    def test_save_multiple_credentials(self):
        self.account_credential.save_account()
        self.new_account_credential = Accounts('Mornica','Mwende','mornicamwende','mwende18')
        self.new_account_credential.save_account()
        self.assertEqual (len(Accounts.account_names),2)

if __name__ == "__main__":
    unittest.main()
       
        
