# Number of subarrays having sum exactly equal to k

def sum(arr,k):
    count=0
    for i in range(0,len(arr)):
        sum=0
        for j in range(i,len(arr)):

            sum+=arr[j]
            if sum == k:
                count+=1
    return count
        
arr = [10, 2, -2, -20, 10]
k = -10
print(sum(arr,k))