"""
删除指定值（双指针方法:快慢指针）
思想:通过循环  快指针是否和指定值相等 如果相等就把快指针的下一个值赋给慢指针
"""
# #导入包
# from typing import List
# #定义删除指定值的函数 函数名为removeDuplicates  传入列表
# def removeDuplicates(nums: List[int],val) -> int:
#     #慢指针slow 初始值为0
#     slow=0
#     #快指针fast 初始值为0
#     fast=0
#     #循环 循环条件为快指针不能超过活着等于列表的总长
#     while fast<len(nums):
#         #判断 下角标为快指针的列表值是否和指定值相等
#         if val==nums[fast]:
#             #快指针下移一步
#             fast+=1
#         #条件不成立时：
#         else:
#             #将快指针的值赋给慢指针
#             nums[slow]=nums[fast]
#             #慢指针下移一步
#             slow += 1
#             #快指针下移一步
#             fast+=1
#     #返回删除指定值后列表的长度
#     return slow
#     #return len(nums)-slow  ##返回删除列表中有几个指定值
# li=removeDuplicates([2,1,2,2,3,4,5,2],2)
# print(li)


"""
删除指定重复值（值交换方法）
思路：通过循环查找列表中判断是否有和指定值不相等的数，用到一个count计数的办法，不相等时进行值的交换
"""
# # 导入包
# from typing import List
# # 定义删除指定值函数
# def remove_val(obj: List, val):
#     # 计数器同时在进行值的交换时也会使用 初始值为0
#     count = 0
#     # 循环列表的下角标
#     for i in range(len(obj)):
#         # 判断 如果列表中的值和指定值不相等时：
#         if obj[i] != val:
#             # 将下角标为count的值和下角标为i的值进行交换  可以把count想象成慢指针 i为快指针
#             obj[count], obj[i] = obj[i], obj[count]
#             count += 1
#     # 返回除指定值外列表中值的个数
#     return count
#     # return len(obj)-count   ##返回列表中有多少个指定值个数
#     # return obj[:count]      ##返回删除指定值后的列表
#     # return obj[count:]       #返回列表中的指定值
# li = remove_val([0, 1, 2, 2, 3, 0, 4, 2], 2)
# print(li)
