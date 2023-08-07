def permutation(arr,pos,size):
    result=[]
    if pos == size:
        return ["".join(arr)]
    else:
        for i in range(pos,size):
            arr[i],arr[pos] = arr[pos],arr[i]
            output = permutation(arr,pos+1,size)
            result.extend(output)
            arr[i],arr[pos] = arr[pos],arr[i]
    return result

arr = ["A","B","C"]
size = len(arr)

print(permutation(arr,0,size))
