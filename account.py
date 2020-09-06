import pyperclip
class Account:
    """
    Class that generates new instances of accounts
    """
    def __init__(self,first_name,last_name,phone_number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    account_list = [] 
    def save_account(self):

        '''
        save_accounts method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list.
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a account that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Account of person that matches the number.
        '''

        for account in cls.account_list:
            if account.phone_number == number:
                return account

    @classmethod
    def account_exist(cls,number):
        '''
        Method that checks if account exists from the account_list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.phone_number == number:
                    return True

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def copy_email(cls,number):
        account_found = Account.find_by_number(number)
        pyperclip.copy(account_found.email)

