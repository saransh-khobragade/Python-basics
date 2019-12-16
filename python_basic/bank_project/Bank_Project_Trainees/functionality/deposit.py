'''
Created on Aug 19, 2015

@author: Seby.Varghese01
'''

from database import viewdb
from validations import viewvalidations
from functionality import payment
from exceptions import CustomException


def transfer_funds(cust_id=None):
    
    
    try:
        display_result=0
        while(display_result==0):
            try:
                input_id=input("enter customer id")
                input_password=input("enter password")
                display_result=viewvalidations.validate_custid_password(input_id,input_password)
                
                
            except CustomException.InvalidUserIdPasswordException as e:
                print(e)
                transfer_funds()
            except CustomException.invalidnumber as e:
                print(e)
                transfer_funds()
            
        
        viewdb.display_accounts(input_id)
        debit_verify=0
        credit_verify=0
        amount_verify=0
        debit_number_verify=0
        credit_number_varify=0
       
        while(debit_verify==0 or credit_verify==0 or amount_verify==0 or debit_number_verify==0 or credit_number_varify==0 ):
            
            
            try:
                
                
                '''--(1)------------------credit account to which amount is to be added is given by user---------------------'''
                
                credit_account=input("Enter the account number to which you want to transfer")
                credit_number_varify=viewvalidations.validateaccno(credit_account)
                
                '''----(2)-----------------transfer amount is given by the user--------------------------------------------------'''
                
                transfer_amount=input("Enter the amount you want to deposit")
                
                
                '''---(3)-----------------debit account from which amount is to be subtracted is given by user----------------------'''
                debit_account=input("Enter the account number from which you want to transfer")
                debit_number_verify=viewvalidations.validateaccno(debit_account)
                
                
                
                '''---(4)-----------------debit account is viewvalidationsed whether belonging to the same user------------------------'''
                debit_verify=viewvalidations.validate_debit_account(debit_account,input_id)
                
                
                '''----(5)----------------credit account is viewvalidationsed whether belonging to the differnt user------------------------'''
                credit_verify=viewvalidations.validate_credit_account(credit_account,debit_account)
                
                
                '''----(6)--------------------amount is viewvalidationsed for range and bdebit balance------------------------------------'''
                amount_verify=viewvalidations.validate_debit_balance(transfer_amount,debit_account)
                
                
                
            except CustomException.invalidtransferammount as e:
                print(e)
                continue
            except CustomException.invalidnumber as e:
                print(e)
                continue
            except CustomException.invalidaccno as e:
                print(e)
                continue
            except CustomException.InvalidCreditAccountException as e:
                print(e)
                continue
            except CustomException.invalidaccounttype as e:
                print(e)
                continue
            except CustomException.LowBalanceException as e:
                print(e)
                continue
            except CustomException.invalidtransferammount as e:
                print(e)
                continue
                
            
            
            
            
        tid=viewdb.perform_transfer(debit_account,credit_account,transfer_amount)
        print("Amount Deposited. Transfer Id is ",tid,".")
        payment_option=input("Do you wish to make a payment? Enter  y or n .")
        if payment_option=='y':
            payment.paymentfunc(input_id)
            
            
    except Exception as e:
        print(e)
        
    
    



