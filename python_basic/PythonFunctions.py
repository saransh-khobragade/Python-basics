
def digitsum(self,number):
    number1=number
    sum=0
    while(number1>0):
            temp=number1%10
            sum+=temp
            number1=number1//10
    return sum

def factorial(number):
    if number<1:
        return
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
    
def digitfactorialsum(number):
    number1=number
    sum=0
    while(number1>0):
            temp=number1%10
            sum+=factorial(temp)
            number1=number1//10
    return sum

def binay_combination(n):
    A=[None]*n
    def combination(n):
        if n<1:
            print(A)
        else:
            A[n-1]=0
            combination(n-1)
            A[n-1]=1
            combination(n-1)
    combination(n)
    
    
def find_leap_years(given_year,upto):
    list_of_leap_years=[]
    #Write your logic here
    flag=0
    
    while(flag==0):
        if (given_year%4==0 and given_year%100!=0) or given_year%400==0:
            for i in range(0,upto):
                list_of_leap_years.append(given_year)
                given_year+=4
            break
        else:
            given_year+=1
    
    return list_of_leap_years



def find_duplicates(list_of_numbers):
    list_of_duplicates=[]
    #Write your logic here

    for i in range(0,len(list_of_numbers)):
        for j in range(0,len(list_of_numbers)):
            if list_of_numbers[i]==list_of_numbers[j] and i!=j and list_of_duplicates.count(list_of_numbers[i])==0:
                list_of_duplicates.append(list_of_numbers[i])
                break
                        
                    
          
    return list_of_duplicates

def convert_currency(amount_needed_inr,current_currency_name):
   
    currency_needed=amount_needed_inr/62.382188
    
    
    if current_currency_name=="Euro":
        equivalent=0.936454
        
    elif current_currency_name=="British Pound":
        equivalent=0.679499
    elif current_currency_name=="Indian Rupee":
        equivalent=62.382188
    elif current_currency_name=="Australian Dollar":
        equivalent=1.298246
    elif current_currency_name=="Canadian Dollar":
        equivalent=1.258377
    else:
        return -1
    
    currency_needed=currency_needed*equivalent
    return currency_needed


def create_largest_number(number_list):
    
    var=""
    for i in number_list:
        number_list.sort(key=None, reverse=True)
    for i in number_list:
        var=str(var)+str(i)

    return int(var)


def check_palindrome(word):
    reverse_string=word[::-1]
    if(reverse_string==word):
        return True
    else:
        return False
   
def find_common_characters(msg1,msg2):
    input1=msg1
    input2=msg2
    
    var=""

    for i in range(0,len(input1)):
        if(input2.find(input1[i])!=-1 and input1[i]!=" "):
            if var.count(input1[i])==0:
                var=var+input1[i]
        
            
    if var=="":
        return -1
    else:
        return var
    
def check_samedigits_onmultiply(number,multiply):
    pass
    num1=int(number)*multiply
    double=str(num1)
    list1=[]
    list2=[]
    for i in str(number): #print(check_samedigits_onmultiply(125874,2))
        list1.append(i)
    for j in double:
         list2.append(j)
        
    set1=set(list1)
    set2=set(list2)
    if set1==set2:
        return True
    else:
        return False
    
def find_pairs_of_numbers(list,sum):
    temp=[] 
    for i in list:
        for j in list:
            if (i+j)==sum and (temp.count([j,i])==0 and temp.count([i,j])==0 and i!=j):
                temp.append([i,j])
    

    for i in range(0,len(temp)):
        if temp[i][0]>temp[i][1]:
            pass
        elif temp[i][0]<=temp[i][1]:
            c=temp[i][1]
            temp[i][1]=temp[i][0]
            temp[i][0]=c
    
    var=""
   
    for i in range(0,len(temp)):
        var=var+"("+str(temp[i][0])+","+str(temp[i][1])+")"
        
    
            
    
    
    if var=="":
        return -1
    else:
        return str(var)
#print(find_pairs_of_numbers([10,20,30,40,50],90))


def sms_encoding(data):
    encoded_data=""
    
    list=[]
    list+=data.split()
    
    var=""
    count=0
    for i in list:
        
        for j in range(0,len(i)):
            
            if i[j]=="a" or i[j]=="e" or i[j]=="i" or i[j]=="o" or i[j]=="u" or i[j]=="A" or i[j]=="E" or i[j]=="I" or i[j]=="O" or i[j]=="U" :
                count+=1
            
        if count==len(i):
            var+=i
        
            
        
        else:
            count=0
            if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u" or i[0]=="A" or i[0]=="E" or i[0]=="I" or i[0]=="O" or i[0]=="U" :
                pass
            else:
                var+=i[0]
            
            
            for j in range(1,len(i)):  
                if i[j]=="a" or i[j]=="e" or i[j]=="i" or i[j]=="o" or i[j]=="u" or i[j]=="A" or i[j]=="E" or i[j]=="I" or i[j]=="O" or i[j]=="U" :
                    pass
                            #print(i[j])
                else:
                            #print(i[j])
                            if (i[j-1]=="a" or i[j-1]=="e" or i[j-1]=="i" or i[j-1]=="o" or i[j-1]=="u" or i[j-1]=="A" or i[j-1]=="E" or i[j-1]=="I" or i[j-1]=="O" or i[j-1]=="U" ):
                               
                                var=var+i[j]
        var=var+" "
    encoded_data=var.strip()
    return encoded_data
#print(sms_encoding("Have a nice day ")) 



def nearest_palindrome(number):
    import math
    stri=""
    num=number+1
    num_str=str(num)
    length=len(str(num))
    x=math.ceil(length/2)
    for i in range(0,x):
        stri=stri+num_str[i]
        continue
    for j in range(x,length):
        stri=stri+num_str[length-j-1]
    if(stri==num_str):
        return num
    else:
        x=nearest_palindrome(num)
    return x

#print(nearest_palindrome(910))



def count_pattern(pat,name_list):
    count2=0
    for i in name_list:
        i.lower()
       
        if i.find(pat)!=-1:
            count2+=1

    return count2
#print(count_pattern("at",["Hat","Cat","rabbit","matter"]))

def check_anagram(data1,data2):
    str1=[]
    str1+=data1.lower()
    str2=[]
    str2+=data2.lower()
    count=0
    flag=0
    
    for i in str1:
        for j in str2:
            if(i==j) and str1.count(j)==1:
                count+=1
    if count==len(str1):
        
        for i in range(0,len(str1)):
            for j in range(0,len(str2)):
                if i==j and str1[i]==str2[j]:
                    flag=1
    else:
        return "False"
    if flag==1:
        return "False"
    else:
        return "True"
#anagram -letter should not repeat at same index        
#print(check_anagram("eat","tea"))



