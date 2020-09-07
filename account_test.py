import pyperclip
import unittest
from account import Account 


class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Andiwo","Edwin","0712248626","andiwoedwin@gmail.com") 
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.account_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"Andiwo")
        self.assertEqual(self.new_account.last_name,"Edwin")
        self.assertEqual(self.new_account.user_account,"0712248626")
        self.assertEqual(self.new_account.password,"andiwoedwin@gmail.com")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("Test","user","0712345678","test@user.com") # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account("Test","user","0712345678","test@user.com") # new account
        test_account.save_account()

        self.new_account.delete_account()# Deleting a account object
        self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_number(self):
        '''
        test to check if we can find a account by user account and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0711223344","test@user.com") # new account
        test_account.save_account()

        found_account = Account.find_by_number("0711223344")

        self.assertEqual(found_account.password,test_account.password)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0711223344","test@user.com") # new account
        test_account.save_account()

        account_exists = Account.account_exist("0711223344")

        self.assertFalse(account_exists)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Account.display_accounts(),Account.account_list)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password address from a found account
        '''

        self.new_account.save_account()
        Account.copy_password("0712345678")

        self.assertEqual(self.new_account.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()