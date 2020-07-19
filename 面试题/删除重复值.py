# """
# 删除重复值（快慢指针方法）
# 思想：将无序列表变成有序列表,在分别给两个指针一个初始值,如果快指针的值和慢指针的值相等就判断快指针的下一项，
#      直到快指针的值和慢指针的值不相等时,把快指针的值赋给慢指针的下一项
#      return slow+1 返回不重复的值有多少个
#      return nums[:slow+1] 返回不重复值的列表
# """
##导入包
# from typing import List
# #定义一个删除重复值的函数 函数名为remove
# def remove(nums:List):
#     #列表进行排序
#     nums.sort()
#     #定义一个慢指针为slow 初始值为0
#     slow=0
#     #定义一个快指针fast 初始值为1
#     fast=1
#     #进行循环 循环条件 fast代表列表的下角标 所以快指针循环次数不能超过或等于列表的总长
#     while fast<len(nums):
#         #判断 如果慢指针的值和快指针的值相等：
#         if nums[slow]==nums[fast]:
#             #让快指针继续往下走  +1
#             fast+=1
#         #条件不成立时
#         else:
#             #慢指针下走一步
#             slow+=1
#             #将快指针的值赋给慢指针
#             nums[slow]=nums[fast]
#             #快指针下走一步
#             fast+=1
#     #返回删除重复值后列表
#     return nums[:slow+1]
# li=remove([1,2,5,2,3,3,3,3,4,4])
# print(li)

"""
删除重复值（切片方法）
思路：有序列表i和i+1相同时，将i+2至列表尾部的值进行切片 将值赋给i+1到尾部的值进行覆盖
"""
# #导入包
# from typing import List
# #定义不重复值类 类命为：removeDupliactd  参数为传入值为列表
# def removeDuplicated(nums: List[int]) -> int:
#     #n为传入列表中的有序不重复值的集合长度  用于下方循环
#     n = len(set(nums))
#     #将传入的列表进行排序
#     nums.sort()
#     #i为一个初始值
#     i = 0
#     #进行循环
#     while i < n-1:
#         #判断 如果第一个数和第二个数相等时：进行切片
#         if nums[i] == nums[i+1]:
#             #temp为临时变量 用于接收重复值
#             temp = nums[i+1]
#             #进行切片
#             nums[i+1:len(nums)-1] = nums[i+2:]
#             #将临时变量temp的值赋给列表的最后一项 ,保证列表的长度原本长度
#             nums[-1] = temp
#             #跳出本次循环
#             continue
#         else:
#             #条件不成立时i能够进行向后移
#             i += 1
#     return i+1
#     #return nums[:i + 1]  ##返回列表的不重复值
#     # return i + 1     ##返回有多少个不重复值
#     # return nums[i + 1:]  ##返回列表中重复的数据
# li=removeDuplicated([1,2,5,2,3,3,3,3,4,4])
# print(li)

