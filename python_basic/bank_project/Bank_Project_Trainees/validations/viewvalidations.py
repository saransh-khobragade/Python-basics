from database import viewdb
from exceptions import CustomException

def validate_login(id1,pas):
    cust=viewdb.get_cust_details(id1)
    if(cust.get_cust_id()==None):
        raise CustomException.Invalidcust_idException
    elif(cust.get_password()==pas):
        return cust
    else:
        raise CustomException.InvalidpasswordException

def validate_age(age):
    if(age>17 and age<96):
        return True
    raise CustomException.InvalidageException
    
def validate_phone(phone):
    
    if(len(str(phone))==10):
        return True
    raise CustomException.InvalidphoneException


def validate_pan(pan,name):
    if(len(str(pan))==10): 
        pan.upper()
        name.upper()
        if(name[0]==pan[4]):
            if(int(pan[5:9])>=0000 and int(pan[5:9])<=9999):
                return True
    raise CustomException.InvalidpanExecption
    

def validate_id(cust_id):
    count=viewdb.count_id(cust_id)
    if count==0:
        raise CustomException.Invalidcust_idException
    else:
        return True
    
def validate_from_acc(cust_id):
    count=viewdb.count_fromacc(cust_id)
    if count==0:
        print("no transaction for this account")
        return False
    else:
        return True

def validate_amount(amount):
    if int(amount)>1000 and int(amount)<100000:
        return True
    else:
        print("The amount should be greater than 1000 and less than 100000")
        return False

 

def validate_fixed_condition(cust_id):
    count=viewdb.count_saving_id(cust_id)
    if count==0:
        raise CustomException.no_saving_account
    count=viewdb.count_fd_id(cust_id)
    if count>10:
        raise CustomException.fd_account_exceeded
    return True


'''-----------------------------------------3 aqnd 4-------------------------------------------'''


def validateaccno(acc_no):
    if(acc_no.isdigit()==True):
        if(viewdb.validacc(acc_no)):
            return True
        else:
            raise CustomException.invalidaccno()
    else:
        raise CustomException.invalidnumber()    
    
def validatebalance(amount,acc_no):
    if(amount.isdigit()==True):
        if(viewdb.validbal(amount,acc_no) ):
            return True
        else:
            raise CustomException.invalidbal()  
    else:
        raise CustomException.invalidnumber()        
'''trainee3'''  
def validate_custid_password(input_id,input_password):
    if(input_id.isdigit()==True):
        disp_result=viewdb.check_custid_password(input_id,input_password)
    
        if disp_result==0:
            raise CustomException.InvalidUserIdPasswordException()
        
        else:
            return True
        return True
    else:
        raise CustomException.invalidnumber()
def validate_debit_account(debit_account,cust_id):
    deb_verify=viewdb.check_debit_account(debit_account,cust_id)
    if deb_verify==0:
        raise CustomException.invalidaccounttype()
  
    else:
        return True
def validate_credit_account(credit_account,debit_account):
    cred_verify=viewdb.check_credit_account(credit_account,debit_account)
    if cred_verify==0:
        raise CustomException.InvalidCreditAccountException()
        
    else:
        return 1
def validate_debit_balance(transfer_amount,debit_account):
    if(1000<=int(transfer_amount)<=10000):
        deb_bal_verify=viewdb.check_balance_after_transfer(transfer_amount,debit_account)
        if deb_bal_verify==0:
            raise CustomException.LowBalanceException()
        
        else:
            return 1 
    else:
        raise CustomException.invalidtransferammount()          
def validate_account_number(acc):
    if(acc.isdigit()):
        return 1
    else:
        raise CustomException.InvalidAcccountNumberException()
        



    
    
    