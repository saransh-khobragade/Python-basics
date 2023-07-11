arr=[1,2,3,4,6,7,8,9]

def findMissingNumberInSeries(arr):
    
    # sum upto n /last element
    n = arr[-1]
    totalSum= int(n*((n+1)/2))
    
    sum=0
    for x in arr:
        sum+=x

    print(totalSum-sum) #Basic sum will be less than sum upto n
findMissingNumberInSeries(arr)


