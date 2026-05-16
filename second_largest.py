def second_largest(arr):
    if len(arr)<2:
        return None
    largest,second_largest=float("-inf"),float("-inf")
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i!=largest and i>second_largest:
            second_largest=i
    return second_largest
val=list(map(int,input().split()))
print(second_largest(val))
