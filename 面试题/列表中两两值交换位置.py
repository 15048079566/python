"""
两两值交换位置（值交换方法）
思路：通过for循环下角标 让步长为2 让循环的下角标的值和下角标的下一个值进行交换
"""
# #导入包
# from typing import List
# #定义一个类 类名为SremoveDuplicates 传入列表
# def removeDuplicates(nums: List[int]) :
#     #判断 如果列表的总长为偶数时：
#     if len(nums)%2==0:
#         #循环列表的下角标 步长为2
#         for i in range(0,len(nums),2):
#             #下角标i和i+1进行值交换
#             nums[i],nums[i+1]=nums[i+1],nums[i]
#     #列表总长为奇数时：
#     else:
#         #循环 循环到列表下角标的前一位 最后一个不进行交换
#         for i in range(0,len(nums)-1,2):
#             #进行值交换
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#     #返回交换值后的列表
#     return nums
# li=removeDuplicates([1,2,3,4,5,6])
# print(li)


"""
两两值交换位置（快慢指针）
思路：进行循环 让快慢指针的每次增加2，慢指针的初始值和快指针的初始值相差1 再将快慢指针的值进行交换
"""
#导入包
from typing import List
#定义函数 函数名为removeDuplicates
def removeDuplicates(nums: List[int]) -> int:
    #慢指针 初始值为0
    slow = 0
    #快指针 初始值为0
    fast = 1
    #循环 快指针的长度小于列表总长
    while fast < len(nums):
        #进行快慢指针值交换
        nums[slow], nums[fast] = nums[fast], nums[slow]
        #慢指针增加2
        slow += 2
        #快指针增加2
        fast += 2
    #返回交换值后的列表
    return nums
li = removeDuplicates([1, 2, 3, 4, 5])
print(li)
