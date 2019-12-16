from validations import viewvalidations
from exceptions import CustomException
from database import viewdb
from functionality import Fixed_deposit

def view_details():
    loop1=True
    loop2=True
    loop3=True
    try: 
        id1=int(input("Enter customer id: "))
        pas=input("Enter your password: ")
        temp_customer_obj=viewvalidations.validate_login(id1,pas)
        print("Name : ",temp_customer_obj.get_name())
        print("Gender: ",temp_customer_obj.get_gender())
        print("Age: ",temp_customer_obj.get_age())
        print("Phone: ",temp_customer_obj.get_phone())
        print("Pan: ",temp_customer_obj.get_pan())
    except CustomException.Invalidcust_idException as e:
        print(e)
        view_details()
    except CustomException.InvalidpasswordException as e:
        print(e)
        view_details()
    except TypeError as e:
        print("Type Error Please Reenter")
        view_details()
    except ValueError as e:
        print("Value Error Please Reenter")
        view_details()
    except IndexError as e:
        print("Index Error Please Reenter")
        view_details()
         
    while(loop1):  
        choice=input("Do you want to update your age,PAN or phone? Press 'Y' or 'N' ")
        if(choice=="Y" or choice=="y"):
            while(loop3):
                try:
                    age=input("Enter new age. Press Enter to skip ")
                    phone=input("Enter new phone. Press Enter to skip ")
                    pan=input("Enter new PAN. Press Enter to skip ")
                    
                    if(len(age)!=0):
                        age=int(age)
                        if(viewvalidations.validate_age(age)):
                            temp_customer_obj.set_age(age)
                    
                    if(len(phone)!=0):
                        
                        if(viewvalidations.validate_phone(phone)):
                            temp_customer_obj.set_phone(phone)
                            
                    if(len(pan)!=0):
                        if(viewvalidations.validate_pan(pan,temp_customer_obj.get_name())):
                            temp_customer_obj.set_pan(pan)
                    viewdb.set_customer_details(temp_customer_obj)
                    print(temp_customer_obj.get_age())
                    print(temp_customer_obj.get_phone())
                    print(temp_customer_obj.get_pan())
                    print("successfully updated")
                    loop1=False
                    loop3=False
                except CustomException.InvalidageException as e:
                    print(e)
                except CustomException.InvalidphoneException as e:
                    print(e)
                except CustomException.InvalidpanExecption as e:
                    print(e)
                except TypeError as e:
                    print("Type Error Please Reenter")
                except ValueError as e:
                    print("Value Error Please Reenter")
                except IndexError as e:
                    print("Index Error Please Reenter")
                
        elif(choice=="N" or choice=="n"):
            break;
        else:
            print(" Invalid key Pressed..")
    while(loop2):
        choice=input("Do you want to open a FD? Press 'Y' or 'N' ")
        if(choice=="Y" or choice=="y"):
            loop2=False
            Fixed_deposit.open_fd(id1)
        elif(choice=="N" or choice=="n"):
            loop2=False
            pass
        else:
            print(" Invalid key Pressed..")
    

        