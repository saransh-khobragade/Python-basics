def twoNumberSum(array, targetSum):
    temp = set(array)
    
    result=[]
    for x in array:
        if targetSum-x in temp and targetSum-x != x:
            result.append(x)
            result.append(targetSum-x)
            break
    return result

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10)) 