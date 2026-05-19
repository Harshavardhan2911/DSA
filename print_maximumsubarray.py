def print_maximumsubarray(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    start,end,temp_start=0,0,0
    for i in range(1,len(arr)):
        if arr[i]>curr_sum:
            curr_sum=arr[i]
            temp_start=i
        else:
            curr_sum=curr_sum+arr[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
            end=i
            start=temp_start
    return arr[start:end+1]
val=list(map(int,input().split()))
print(print_maximumsubarray(val))