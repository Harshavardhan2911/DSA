def maximum_subarray_sum(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        curr_sum=max(curr_sum+arr[i],arr[i])
        max_sum=max(max_sum,curr_sum)
    return max_sum
val=list(map(int,input().split()))
print(maximum_subarray_sum(val))