from exceptions import CustomException
from validations import viewvalidations
'''
positive test cases
'''
viewvalidations.validate_id(100)
viewvalidations.validate_from_acc(502)
viewvalidations.validate_amount(1200)

try:
        viewvalidations.validate_fixed_condition(501)
    
except CustomException.Invalidcust_idException as e:
        print(e)
except CustomException.no_saving_account as e:
        print(e)
except Exception as e:
        print(e)



 
'''
negative test cases
'''
 
def run():
    try:
        viewvalidations.validate_id(1001)
    except CustomException.Invalidcust_idException as e:
        print(e)
    except CustomException.no_saving_account:
        print(e)
    except Exception as e:
        print(e)
    
    
    try:
        viewvalidations.validate_from_acc(507)
    except CustomException.no_transaction_of_account as e:
        print(e)
         
     
    try:
        viewvalidations.validate_amount(1)
        
    except Exception as e:
        print(e)
    
    try:
        viewvalidations.validate_amount(167457456456)
        
    except Exception as e:
        print(e)
        
    try:
        viewvalidations.validate_fixed_condition(5)
    
    except CustomException.Invalidcust_idException as e:
        print(e)
    except CustomException.no_saving_account as e:
        print(e)
    except Exception as e:
        print(e)

run()