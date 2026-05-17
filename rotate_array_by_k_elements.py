def rotate_array(arr,k):
    return arr[k:]+arr[:k]
val=list(map(int,input().split()))
k=int(input())
print(rotate_array(val,k))
