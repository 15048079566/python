"""
两两值交换位置（快慢指针）
思路：进行循环 让快慢指针的每次增加2，慢指针的初始值和快指针的初始值相差1 再将快慢指针的值进行交换
"""
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    slow = 0
    fast = 1
    while fast < len(nums):
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 2
        fast += 2
    return nums
li = removeDuplicates([1, 2, 3, 4, 5])
print(li)
