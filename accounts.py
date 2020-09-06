

class Accounts:
    account_names = []
    def __init__(self, first_name, last_name, user_name, password):

        '''
        Methods to define the properties for each user object will hold.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

#     user_accounts = []

    def save_account(self):
        Accounts.account_names.append(self)
    
#     def delete_account(self):
#         Accounts.user_accounts.remove(self)


# class Password:
#     '''
#     Class to create account passwords and save their information.
#     '''

#     passwords_list
