"""
指定值求列表中两数之和（字典方法）
思路：指定值减去列表中的每一个值 存入到字典当中key就是差值value就是列表的下角标  在字典中查询差值 返回差值对应的value值就是下角标
"""
# #定义函数 函数名为twoSum
# def twoSum(nums,target):
#     #新建一个空字典
#     nums_dict={}
#     #遍历列表下角标
#     for i in range(len(nums)):
#         #temp作为临时变量 存指定值减去列表中的值
#         temp=target-nums[i]
#         #如果差值在字典当中
#         if temp in nums_dict:
#             #返回下角标和字典中的value值
#             return [i,nums_dict[temp]]
#         #否则
#         else:
#             nums_dict[nums[i]]=i
# li=twoSum([1,2,4,5,6],6)
# print(li)

"""
指定值求列表中两数之和（对撞指针）
思路:左指针为0开始，右指针从列表最后开始，指定值减去右指针值如果大于做指针值 那就左指针下移一步，否则右指针前移一步
"""
# #定义函数 函数名为twoSum 传入有序列表和指定值
# def twoSum(nums:list,target):
#     #左指针 初始值为0
#     left=0
#     #右指针 初始值为列表总长减1
#     right=len(nums)-1
#     #循环条件 左指针小于右指针
#     while left<right:
#         #如果指定值-右指针>做指针 就说明左指针的值小于最终的结果 所以做指针向下移一步
#         if target-nums[right]>nums[left]:
#             left+=1
#         #否则 说明右边的值过于大 所以让右指针前移一步
#         else:
#             right-=1
#         #判断 左指针的值加右指针的值等于指定值的时
#         if nums[left]+nums[right]==target:
#             #打印左指针和右指针
#             print([left,right])



"""
指定值求列表中两数之和（暴力破解法）
思路：两个循环 第一个值和列表中所有值进行对比 符合条件的打印出来 以此类推
"""
# #定义函数 函数名为twoSum 传入列表 和指定值
# def twoSum(nums:list,target):
#     #遍历列表下角标
#     for i in range(len(nums)):
#         #遍历列表下角标 从i+1开始 优化
#         for j in range(i+1,len(nums)):
#             #如果符合条件
#             if nums[i]+nums[j]==target:
#                 #返回i和j
#                 return [i,j]
# li=twoSum([1,2,4,5,6],6)
# print(li)


"""
指定值求列表中两数之和（对撞指针和index查找下标）
思路：查找这两个数是啥，在用index在列表中查找下标
"""
# #导入包
# from  typing import List
# #定义函数 函数名为twoSum  传入列表和指定值
# def twoSum(numbers: List[int], target: int) -> List[int]:
#     #对原列表进行切片不会影响原列表的值
#     num1=numbers[:]
#     #对原列表进行反向切片 用于列表中含有重复值查找
#     num2=numbers[::-1]
#     #对num1列表进行排序
#     num1.sort()
#     #左指针
#     left = 0
#     #右指针
#     right=len(num1)-1
#     #循环
#     while left<right:
#         # 如果指定值-右指针>做指针 就说明左指针的值小于最终的结果 所以做指针向下移一步
#         if target-num1[right]>num1[left]:
#             left+=1
#         #左指针的值加右指针的值等于指定值时：
#         elif num1[left]+num1[right]==target:
#             #a为临时变量 从原列表中查找左指针值对应的下标
#             a=numbers.index(num1[left])
#             #b为临时变量 要从num2列表中查找 如果列表中有重复值 会导致程序出错 所以反向查找 再用原列表长度减反向查找的下标 就是要求的下标
#             b=(len(num2)-1)-num2.index(num1[right])
#             #返回a、b下标
#             return [a,b]
#         # 否则说明右边的值过于大所以让右指针前移一步
#         else:
#             right-=1
# li = twoSum([-1, -2, -3, -4, -5], -8)
# print(li)