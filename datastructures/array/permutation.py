def permute(arr,pos,size):
        result=[]
        if pos == size:
            return [[*arr]]
        else:
            for i in range(pos,size):
                arr[i],arr[pos] = arr[pos],arr[i]
                result.extend(permute(arr,pos+1,size))
                arr[i],arr[pos] = arr[pos],arr[i]
        return result
print(permute([1,2,3],0,3))