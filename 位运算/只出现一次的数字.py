"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
思路：两个同样的数字进行异或运算会返回0  0与数字进行异或运算还是数字本身 所以会返回不重复的数字
"""
#定义函数名 函数名为singleNumber
def singleNumber( nums):
    #res初始值为0 因为在进行异或运算时 不会影响数据 同时也是一个变量
    res=0
    #进行遍历
    for i in nums:
        #进行异或运算 
        res=res ^ i
    #返回不重复数字
    return res
print(singleNumber([1,2,1,2,5]))