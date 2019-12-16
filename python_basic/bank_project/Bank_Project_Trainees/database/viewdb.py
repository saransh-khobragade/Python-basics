from utility import DBConnectivity
from classes.CustomerModule import Customer
from utility import DateUtility

def get_cust_details(id1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select cust_id,password,name,gender,phone,pan,age from customer where cust_id=:cid",{"cid":id1})
        c=Customer()
        for temp in cur:
            c.set_cust_id(temp[0])
            c.set_password(temp[1])
            c.set_name(temp[2])
            c.set_gender(temp[3])
            c.set_phone(temp[4])
            c.set_pan(temp[5])
            c.set_age(temp[6])                      
            
    finally:
        cur.close()
        con.close()
        return c

def set_customer_details(obj):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update customer set age=:p_age,phone=:p_phone,pan=:p_pan where cust_id=:p_id",
                    {"p_phone":obj.get_phone(),"p_pan":obj.get_pan(),"p_age":obj.get_age(),"p_id":obj.get_cust_id()})
    finally:
        cur.close()
        con.commit()
        con.close()  

def count_id(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("select count(cust_id) from customer where cust_id=:cid",{"cid":cust_id})
    for w in cur:
        temp=w[0]
        
    
    cur.close()
    con.close()
    return temp

def count_fromacc(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("select count(From_account) from transactions where From_account=:cid",{"cid":cust_id})
    for w in cur:
        temp=w[0]
        
    
    cur.close()
    con.close()
    return temp

def max_id(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("select max(Account_number) from Account")
    for w in cur:
        temp=w[0]
        
    
    cur.close()
    con.close()
    return temp

def count_saving_id(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    
    cur.execute("select count(cust_id) from Account where Account_type='Savings' and cust_id=:cid",{"cid":cust_id})
    for w in cur:
        temp=w[0]
        
    
    cur.close()
    con.close()
    
    return temp
#count_saving_id(100)
 
def count_fd_id(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("select count(cust_id) from Account where Account_type='FD' and cust_id=:cid",{"cid":cust_id})
    for w in cur:
        temp=w[0]
        
    
    cur.close()
    
    con.close()
    return temp

def insert_fd(cust_id, amount):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    count=max_id(cust_id)
    cur.execute("insert into ACCOUNT values("+str(cust_id)+","+str(count+1)+","+str(amount)+",to_date('"+DateUtility.get_todays_date()+"','DD-mm-yyyy'),'FD')")
    print("FD opened successfuly with ACC No: ",count+1)
    
    cur.close()
    con.commit()
    con.close()
    
    return True
            

'''-------------------------------------------------3 and 4--------------------------------------------------------------'''

def validacc(acc_no):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select count(account_number) from account where account_type='Savings' and account_number=:acc_no",{"acc_no":int(acc_no)})
        for j in cur:
            if(j[0]==0):
                #print("kj")
                return False
            else:
                return True
    finally:
        cur.close()
        con.close()
def validbal(amount1,acc_no):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur5=DBConnectivity.create_cursor(con)
        cur.execute("select amount from account where account_type='Savings' and account_number=:acc_no",{"acc_no":acc_no})
        for j in cur:
            if(j[0]-int(amount1)<1000):
                return False
                #raise customException.invalidbal()
            else:
                
                #print(j[0]-int(amount1))
                cur5.execute("update account set amount=amount-"+amount1+ "where account_number=:acc_no",{"acc_no":acc_no})
                return True
    finally:
        con.commit()
        cur.close()
        cur5.close()
        con.close()     
def inserttable(acc_no,amount,desc):  
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        cur3=DBConnectivity.create_cursor(con)
        cur.execute("select max(payment_id) from payment")
        for value in cur:
            if(value[0]==None):
                pid=5
                cur2.execute("insert into payment (Payment_id,Account_number,Payment_amount,Description_of_payment) values(:pay_d,:acc_no,:amount,:descri)",{"pay_d":pid,"acc_no":int(acc_no),"amount":int(amount),"descri":desc})
                return pid 
            else: 
                pid=value[0]+1
                cur3.execute("insert into payment (Payment_id,Account_number,Payment_amount,Description_of_payment) values(:pay_d,:acc_no,:amount,:descri)",{"pay_d":pid,"acc_no":int(acc_no),"amount":int(amount),"descri":desc})
                return pid
               
    finally:
        con.commit()
        cur.close()
        cur2.close()
        cur3.close()
        con.close()
        
        
'''trainee3'''
def check_custid_password(input_id,input_password):
    try:
        f=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        cur.execute("select name from customer where cust_id="+input_id+" and password="+input_password)
        print("jsfdfjdgsjfgsdgfjsdgfjsdgf")
        name=cur.fetchall()
        if len(name)==0:
                f=0
        else:
            f=1
        return f 
    finally:
        cur.close()
        con.close()
            
def check_debit_account(debit_account,cust_id):
    try:
        f=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select account_number from account where account_type='Savings' and cust_id="+cust_id+"and account_number="+debit_account)
        
        
        a=cur.fetchall()
    
        if a==[]:
            f=0
        else:
            f=1
         
    finally:
        cur.close()
        con.close()
    return f      

        
        


def display_accounts(input_id):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)        
        print("The available savings account are:")
        cur.execute("select account_number,account_type,amount from account where account_type='Savings' and cust_id=:input_id ",
                      {"input_id":input_id})
        for row in cur:
            print(row)
               
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
    


def check_credit_account(credit_account,debit_account):
    try:
        f=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select * from account where account_type='Savings' and account_number=:credit_account",
                    {"credit_account":credit_account})
        
        
        a=cur.fetchall()
        if a==[] or (credit_account==debit_account):
            f=0
        else:
            f=1
            
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
    return f


def check_balance_after_transfer(transfer_amount,debit_account):
    try:
        f=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
    
        cur.execute("select amount from account where account_type='Savings' and account_number=:debit_account",
                    {"debit_account":debit_account})
        
        
        
        a=cur.fetchall()
        
        if ( int(a[0][0])-int(transfer_amount) )<1000:
            f=0
        else:
            f=1
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()
    return f

def perform_transfer(debit_account,credit_account,transfer_amount):
    try:
        
        con=DBConnectivity.create_connection()
        cur1=DBConnectivity.create_cursor(con)
        cur1.execute("update account set amount=amount-(:transfer_amount) where account_number=:debit_account",
                    {"debit_account":debit_account,"transfer_amount":transfer_amount})
        cur1.execute("update account set amount=amount+(:transfer_amount) where account_number=:credit_account",
                    {"credit_account":credit_account,"transfer_amount":transfer_amount})
        
        
        
        cur1.execute("select count(Transaction_id)  from transactions ")
        a=cur1.fetchall()
        print(a)
        f=0
        
        if ( a[0][0] )!=0:
            cur1.execute("select max(transaction_id)  from transactions")
            b=cur1.fetchall()
            c=(int(b[0][0])+int(1) )
            cur1.execute("insert into transactions values("+str(c)+","+debit_account+","+credit_account+",to_date('"+DateUtility.get_todays_date()+"','DD-mm-yyyy') ,"+transfer_amount+")")
            f=c
        else:
            print(DateUtility.get_todays_date())
            cur1.execute("insert into transactions values(1,"+debit_account+","+credit_account+",to_date('"+DateUtility.get_todays_date()+"','DD-mm-yyyy'),"+transfer_amount+")")
            f=1
            
    except Exception as e:
        print(e)
    finally:
        cur1.close()
        con.commit()
        con.close()
    return f

def transaction(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    list_of_transactions=[]
    cur.execute("select from_account,to_account,transfer_amount,Date_of_transaction  from transactions where From_account=:from_acc",{"from_acc":cust_id})

    for row in cur:
        list_of_transactions+=[[row[0],row[1],row[2],row[3]]]
    cur.close()
    con.close()
    return list_of_transactions

def amount_transaction(cust_id):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    
    cur.execute("select transfer_amount  from transactions where From_account=:from_acc",{"from_acc":cust_id})
    for w in cur:
        
        temp=w[0]

    return temp

