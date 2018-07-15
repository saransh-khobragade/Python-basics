from functionality import Fixed_deposit
from functionality import viewfunctions  
from functionality import deposit
from functionality import payment
from functionality import View_and_flow

print("Welcome to Infy Bank!!")
print("Choose an option from below:\n")
end=False
while(end==False):
    print("1. View and Update my details")
    print("2. Open a FD")
    print("3. Transfer Funds")
    print("4. Make a payment")
    print("5. View fund flow")
    print("6. Exit")
    option=input()
    if(option.isdigit() and (int(option)>=1 and int(option)<=6)):
        
        if(int(option)==1):
            print("View my details")
            viewfunctions.view_details()  
                
        if(int(option)==2):
            print("Open FD")
            Fixed_deposit.direct_open_fd()
            
        if(int(option)==3):
            print("Transfer Funds")
            deposit.transfer_funds()
            
        if(int(option)==4):
            print("Make a payment")
            payment.paymentfunc()
            
        if(int(option)==5):
            print("View fund flow")
            View_and_flow.display()
            
        if(int(option)==6):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3,4,5,6 )")
    
