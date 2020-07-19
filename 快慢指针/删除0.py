"""
删除0（双指针方法：快慢指针）
思路：通过循环 快指针是否和指定值相等 如果相等就把快指针的下一个值赋给慢指针
"""
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    var=0
    slow=0
    fast=0
    while fast<len(nums):
        if var==nums[fast]:
            fast+=1
        else:
            nums[slow],nums[fast]=nums[fast],nums[slow]
            fast+=1
            slow+=1
    return nums[:slow]
    # return nums[slow:]  #返回删除的指定元素
    # return slow  #返回删除0后列表的长度
    # return len(nums)-slow  #返回列表中有几个0
li=removeDuplicates([0,1,0,1,2,3])
print(li)