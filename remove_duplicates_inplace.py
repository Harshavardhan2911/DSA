def remove_duplicates_inplace(arr):
    left=0
    for right in range(1,len(arr)):
        if arr[right]!=arr[left]:
            left+=1
            arr[left]=arr[right]
    return arr[:left+1]
val=list(map(int,input().split()))
print(remove_duplicates_inplace(val))