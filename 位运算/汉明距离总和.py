"""
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
计算一个数组中，任意两个数之间汉明距离的总和。
思路：两个循环 让两个数进行计算汉明距离 在进行总和相加
"""
#定义函数名 函数名为totalHammingDistance
def totalHammingDistance(nums):
    #计数器
    count = 0
    #遍历下标 两个循环
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            #判断相同位置上的两个数是否相同就用异或运算 相同的数为0  不相同为1 接下来删除1的次数 就是相同位置上不同数的次数
            a = nums[i] ^ nums[j]
            while a != 0:
                #删除1 就用a&（a-1）
                a = a & (a - 1)
                #去掉一个1 计数就增加1
                count += 1
    #返回汉明距离总和
    return count
li=totalHammingDistance([4,12,2])
print(li)



"""
汉明距离总和 优化版
"""
def totalHammingDistance(nums):
    #总和输出结果
    res=0
    #一个整型4字节 1个字节8个bit
    for i in range(32):
        #用于计算二进制中0的个数
        count_0 = 0
        #用于计算二进制1的个数
        count_1 = 0
        for j in range(len(nums)):
            #转二进制>>向后移i位
            if (nums[j]>>i)&1:
                #是1的时候 +1
                count_1+=1
            else:
                #是0的时候就+1
                count_0+=1
        #最后的最后总和
        res=res+count_0*count_1
    return res
li=totalHammingDistance([4,12,2])
print(li)