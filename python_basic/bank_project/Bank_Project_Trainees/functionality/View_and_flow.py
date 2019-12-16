from validations import viewvalidations
from database import viewdb
from exceptions import CustomException
count=0

amt=0
total=0

def display():
    try:
        while(1):
            cust_id=input("Enter Account no.")
            if viewvalidations.validate_from_acc(cust_id):
                count=0
                total=viewdb.amount_transaction(cust_id)
                
                flow(cust_id)
                break
    
    except CustomException.Invalidcust_idException as e:
        print(e)
    except Exception as e:
        print(e)

def flow(cust_id):
    global count
    global count
    global amt
    
    if count>30 and amt>total:
        return                                                                                                  #for restricting upto 2 levels
    var=""
    
    for j in range(0,count):
            var+="   "

    count=count+5
    for i in viewdb.transaction(cust_id):
        amt+=int(i[2])
        
        print(var)
        print(var+"Amount "+str(i[2])+"  transfered from "+str(i[0])+" to "+str(i[1])+"   on  "+str(i[3]))
        flow(i[1])                                                                                           #recursion
    print(count)
