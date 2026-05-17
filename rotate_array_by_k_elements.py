def rotate_array(arr,k):
    rotate=k%len(arr)
    return arr[rotate:]+arr[:rotate]
val=list(map(int,input().split()))
k=int(input())
print(rotate_array(val,k))
