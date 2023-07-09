def isAnagram(str1,str2):
    temp={}
    flag=True
    
    # Count frequency of all elements
    for x in str1:
        if x in temp:
            temp[x]+=1
        else:
            temp[x]=1
    
    # decreament frequency of all elements
    for x in str2:
        if x in temp:
            temp[x]-=1
        else:
            temp[x]=1
    
    # if there is any count its not anagram
    for x,y in temp.items():
        if y>0:
            flag=False
    
    return flag


str1="abbc"
str2="acbb"
print(isAnagram(str1,str2))


def isAnagram(str1,str2):
    d={}
    for x in str1:
        if d[x]:
            d[x]+=1
        else:
            d[x]=1
    print(d)
       



str1="abbc"
str2="acbb"
isAnagram(str1,str2)
