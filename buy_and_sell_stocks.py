
def buy_and_sell_stocks(arr):
    buy=arr[0]
    max_profit=float("-inf")
    for i in range(1,len(arr)):
        sell=arr[i]-buy
        max_profit=max(max_profit,sell)
        buy=min(buy,arr[i])
    if max_profit<0:
        return 0
    return max_profit
val=list(map(int,input().split()))
print(buy_and_sell_stocks(val))