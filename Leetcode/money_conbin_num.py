#动态规划，input一个总金额，output一个以nums数组里面金额为基础金额的钱的数目
def sovle(n):
    nums=[1,5,10,20,50,100]
    data = [0] * (n+1)
    data[0] = 1
    print(data)
    for num in nums:
        for i in range(n+1):
            if i-num>=0:
                data[i] += data[i-num]
                print(i,num,data)
    return data[-1]
nums = int(input())
print(sovle(nums))
