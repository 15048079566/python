"""
删除两个重复值（快慢指针）
思路：通过循环 快指针进行移动 同时判断有几个重复值，当重复值大于2个时从第3个重复值进行替换
"""
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    show = 0
    nums.sort()
    fast=1
    count=1
    while fast<len(nums):
        if nums[show]==nums[fast]:
            if count>=2:
                fast+=1
            else:
                count+=1
                show+=1
                nums[show]=nums[fast]
                fast+=1
        else:
            count=1
            show+=1
            nums[show]=nums[fast]
            fast+=1
    return show+1
li=removeDuplicates([0,1,0,1,2,3,0,1])
print(li)