def majority_element(arr):
    candidate=arr[0]
    count=0
    for i in range(len(arr)):
        if arr[i]==candidate:
            count+=1
        else:
            count+=-1
        if count==0:
            candidate=arr[i]
            count=1
        if arr.count(candidate)>len(arr)//2:
            return candidate
    return -1
val=list(map(int,input().split()))
print(majority_element(val))