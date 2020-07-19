"""编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
思路：十进制转二进制 再用二进制中n&（n-1）中有记录多少个1
"""
#定义函数名 函数名为hammingWeight 传入不为0的整数
def hammingWeight(n):
    #计数器
    count=0
    #n不等于0的时候进行循环
    while n!=0:
        #举个例子n=5 二进制就是 101 n-1就是100 与运算就是100 一次类推
        n=n&(n-1)
        #每次减去1 用计数器增加1
        count+=1
    #返回最后结果
    return count
ha=hammingWeight(5)
print(ha)