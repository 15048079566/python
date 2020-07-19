"""
删除重复值（快慢指针方法）
思想：将无序列表变成有序列表,在分别给两个指针一个初始值,如果快指针的值和慢指针的值相等就判断快指针的下一项，
     直到快指针的值和慢指针的值不相等时,把快指针的值赋给慢指针的下一项
     return slow+1 返回不重复的值有多少个
     return nums[:slow+1] 返回不重复值的列表
"""
from typing import List
def remove(nums:List):
    nums.sort()
    slow=0
    fast=1
    while fast<len(nums):
        if nums[slow]==nums[fast]:
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]
            fast+=1
    return nums[:slow+1]
li=remove([1,2,5,2,3,3,3,3,4,4])
print(li)