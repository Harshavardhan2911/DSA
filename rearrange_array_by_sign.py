def rearrange_array_by_sign(arr):
    res=[0]*len(arr)
    positive=0
    negative=1
    for i in arr:
        if i>0:
            res[positive]=i
            positive+=2
        else:
            res[negative]=i
            negative+=2

    return res
val=list(map(int,input().split()))
print(rearrange_array_by_sign(val))