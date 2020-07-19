"""
删除指定值（双指针方法:快慢指针）
思想:通过循环  快指针是否和指定值相等 如果相等就把快指针的下一个值赋给慢指针
"""
from typing import List
def removeDuplicates(nums: List[int],val) -> int:
    slow=0
    fast=0
    while fast<len(nums):
        if val==nums[fast]:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow += 1
            fast+=1
    return slow
li=removeDuplicates([2,1,2,2,3,4,5,2],2)
print(li)