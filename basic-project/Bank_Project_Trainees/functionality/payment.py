'''
Created on Aug 19, 2015

@author: shashank.ramteke
'''

import string
import random
from exceptions import CustomException
from validations import viewvalidations
from database import viewdb
def paymentfunc(custid=None):
    if(custid==None):
        end=False
        while end==False:
            try:
                custid=input("enter customer id :")
                password=input("enter your password:")
                ''' method for validation'''
            
                if(viewvalidations.validate_custid_password(custid,password)):
                    end=True
                    paymentfunc2(custid)
                else:
                    end=False 
            except CustomException.InvalidUserIdPasswordException  as  e:
                print(e)   
            except CustomException.invalidnumber as e:
                print(e)
                paymentfunc()
                
    else:
        paymentfunc2(custid)    
def paymentfunc2(custid):     
    try:
        
        end=False
        while (end==False):
            acc_no=input("Enter Account number: ")
            if(viewvalidations.validateaccno(acc_no)):
                
                if(viewvalidations.validate_debit_account(acc_no,custid)):
                    end=True
                    print("Enter the Amount:")
                    pc=0 
                    while (pc==0):
                        amount=input()
                        if(viewvalidations.validatebalance(amount,acc_no)):
                            pc=1
                            flag=0
                            while(flag==0):
                                x=random.randrange(1,9)
                                y=random.choice(string.ascii_letters)
                                z=random.randrange(100,999)
                                q1=(str(x)+str(y.upper())+str(z))
                                print("Captcha:",q1)
                                q2=input("Enter the Captcha: ")
                                if(q1!=q2):
                                    flag=0
                                    print("incorrect! Reenter the captcha")
                                else:
                                    flag=1
                                    end=True
                                    i=input("Enter  Description :")
                                    payid=viewdb.inserttable(acc_no,amount,i)
                                    print("payment was successful with id:",payid)
                                    
                                           
                        else:
                            print("Re-enter the amount")
                            pc=0
                                    
                else:
                    print("Re-Enter your account number")
                    end=False       
               
    except CustomException.invalidaccno as e:
            print(e) 
            paymentfunc2(custid)
    except CustomException.invalidbal as e:
        print(e)  
        paymentfunc2(custid)    
    except  CustomException.invalidnumber as e:
        print(e)                                       
        paymentfunc2(custid)   
    except  CustomException.invalidaccounttype as e:
        print(e)
        paymentfunc2(custid) 
    finally:
        pass          
                    
                