#!/usr/bin/env python3.8
from account import Account

def create_account(fname,lname,phone,password):
    '''
    Function to create. new account
    '''
    new_account = Account(fname,lname,phone,password)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()

def find_account(number):
    '''
    Function that finds a account by number and returns the account
    '''
    return Account.find_by_number(number)

def check_existing_accounts(number):
    '''
    Function that check if a account exists with that number and return a Boolean
    '''
    return Account.account_exist(number)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()


def main():
    print("Hello! Welcome to your account list. What is your name?")
    user_name = input()
    print("Hello "+ user_name + " what would you like to do?")
    print('\n')
    while True:
                    print("Follow the following short codes : cna- create a new account, da - display accounts, fa -find a account, ex -exit the account ")
                    short_code = input().lower()
                    if short_code == 'cna':
                            print("New Account")
                            print("-"*10)
                            print ("First name ....")
                            f_name = input()
                            print("Last name ...")
                            l_name = input()
                            print("user account ...")
                            p_number = input()
                            print("password ...")
                            e_address = input()
                            save_accounts(create_account(f_name,l_name,p_number,e_address)) # create and save new account.
                            print ('\n')
                            print(f_name + l_name + "your account has been created")
                            print ('\n')
                    elif short_code == 'da':
                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')
                                    for account in display_accounts():
                                        print("Name: account.first_name + account.last_name")
                                        print("user account: contact.user_account")
                                    print("password : account.password")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')
                    elif short_code == 'fa':
                            print("Enter the account you want to search for")
                            search_account = input()
                            if check_existing_accounts(search_account):
                                    search_account = find_account(search_account)
                                    print("search_account.first_name + search_account.last_name")
                                    print('-' * 20)
                                    print("user account....... search_account.user_account")
                                    print("password.......search_account.password")
                            else:
                                    print("That account does not exist")
                    elif short_code == "ex":
                            print("See you then .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()
