'''
Created on Aug 21, 2015

@author: Seby.Varghese01
'''
'''
Created on Aug 21, 2015

@author: Seby.Varghese01
'''

class Invalidcust_idException(Exception):
    def __init__(self):
        super().__init__("The customer id is invalid")
        
class InvalidpasswordException(Exception):
    def __init__(self):
        super().__init__("The password is invalid")

class InvalidageException(Exception):
    def __init__(self):
        super().__init__("The age is invalid")
        
class InvalidphoneException(Exception):
    def __init__(self):
        super().__init__("The phone is invalid")
        
class InvalidpanExecption(Exception):
    def __init__(self):
        super().__init__("The pan is invalid")

class fd_account_exceeded(Exception):
    def __init__(self):
        super().__init__("Customer already has more than 10 fixed account")

class no_saving_account(Exception):
    def __init__(self):
        super().__init__("Customer should have atleast one saving account")
        
class no_transaction_of_account(Exception):
    def __init__(self):
        super().__init__("Customer should have atleast one saving account")
        
        
'''------------------------------------3 AND 4----------------------------------------'''
class invalidaccno(Exception):
    def __init__(self):
        print("invalid account")

        
class invalidbal(Exception):
    def __init__(self):
        print("insufficient balance!reenter your account number")

class invalidnumber(Exception):
    def __init__(self):
        print("wrong input data type! please reenter your number")
'''
trainee 3 
'''
class InvalidUserIdPasswordException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong id and password.Re enter values.\n") 

class invalidaccounttype(Exception): 
    def __init__(self):
        print("wrong account type")
          
class InvalidCreditAccountException(Exception):
    def __init__(self):
        super().__init__("\nYou have entered wrong credit account.\nYou can transfer funds to savings account of other customers only.\nRe enter values.\n")
        
        
class LowBalanceException(Exception):
    def __init__(self):
        super().__init__("\nThere must be at least 1000 balance in the account after the transfer.\n")


class InvalidAcccountNumberException(Exception):
    def __init__(self):
        super().__init__("\nThe amount you have entered is invalid.\nIt should be integer value and among the account numbers only.\n")
        
class invalidtransferammount(Exception):
    def __init__(self):
        super().__init__("reneter values")      
        
class InvalidAmountNumberException(Exception):
    def __init__(self):
        super().__init__("\nThe number you have entered is invalid.\nIt should be integer value and among the account numbers only.\n")