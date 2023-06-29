def isAnagram(str1,str2):
    temp={}
    flag=True
    for x in str1:
        if x in temp:
            temp[x]+=1
        else:
            temp[x]=1
    
    for x in str2:
        if x in temp:
            temp[x]-=1
        else:
            temp[x]=1
    
    for x,y in temp.items():
        if y>0:
            flag=False
    
    return flag


str1="abbc"
str2="acbb"
print(isAnagram(str1,str2))


