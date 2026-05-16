def largest(arr):
    maximum=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
    return maximum
val=list(map(int,input().split()))
print(largest(val))