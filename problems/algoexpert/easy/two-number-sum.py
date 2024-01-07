def twoNumberSum(array, targetSum):
    
    result = []
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i]!=array[j] and array[j]==targetSum-array[i]:
                result.append(array[i])
                result.append(array[j])
    return result
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10)) 