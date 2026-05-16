def move_zeroes_to_end(arr):
    left=0
    for right in range(len(arr)):
        if arr[right]!=0:
            arr[right],arr[left]=arr[left],arr[right]
            left+=1
    return arr
val=list(map(int,input().split()))
print(move_zeroes_to_end(val))