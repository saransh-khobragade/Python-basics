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
