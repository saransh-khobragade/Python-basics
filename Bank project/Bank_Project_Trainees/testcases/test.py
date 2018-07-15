'''
Created on Aug 20, 2015

@author: sandeep.nerella
'''
from validations import viewvalidations
from exceptions.CustomExceptions import Invalidcust_idException
from exceptions.CustomExceptions import InvalidpasswordException
from exceptions.CustomExceptions import InvalidageException
from exceptions.CustomExceptions import InvalidphoneException
from exceptions.CustomExceptions import InvalidpanExecption

#print("Psitive Test case","100,1000","expected_output-Successful","validate_login(id,pas)")
#print(viewvalidations.validate_login())



print("Psitive Test case","24","expected_output-true","validate_age(24)")
print(viewvalidations.validate_age(24))

try:
    print("negative Test case","12","expected_output-true","validate_age(12)")
    print(viewvalidations.validate_age(12))
except InvalidageException as e:
    print(e)
finally:
    print("Enter valid age")