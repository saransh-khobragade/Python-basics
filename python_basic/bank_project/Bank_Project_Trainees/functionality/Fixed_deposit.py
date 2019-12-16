from validations import viewvalidations
from database import viewdb
from exceptions import CustomException
from functionality import deposit

def open_fd(cust_id):
    try:
        while(1):
            amount=input("Enter Amount")
            if amount!="":
                if viewvalidations.validate_id(cust_id) and viewvalidations.validate_amount(amount):
                    
                    if add_fixed_account(cust_id,amount):
                        break
            else:
                print("please enter some amount in number")
                
                
      
        choice=input("Do you wish to transfer funds? Enter 'Y' or 'N' ")
        if(choice=="Y"):
            deposit.transfer_funds(cust_id)
        
   
    except TypeError as e:
        print("type")
    except ValueError as e:
        print("please enter some amount in number")
        open_fd(cust_id)
    except CustomException.Invalidcust_idException as e:
        print(e)
    except Exception as e:
        print(e)
        
 
def direct_open_fd():
    while(1):
        try:
            cust_id=int(input("Enter customer id: "))
            if viewvalidations.validate_id(cust_id):
                open_fd(cust_id)
                break
        except ValueError:
            print("The customer id is invalid")
        except CustomException.Invalidcust_idException as e:
            print(e)
        except Exception as e:
            print(e)
        
def add_fixed_account(cust_id,amount):
    try:
        if viewvalidations.validate_fixed_condition(cust_id):
                if viewdb.insert_fd(cust_id, amount):
                    return True
                
    except CustomException.Invalidcust_idException as e:
        print(e)
    except CustomException.no_saving_account as e:
        print(e)
    except CustomException.fd_account_exceeded as e:
        print(e)
        print("Customer cant have more accounts")
        return True
        
    except Exception as e:
        print(e)
        print(" Error in add fixed condition")
    