"""
替换列表中任意两个数
思路：首先思考传入的列表的下标是否越界，在进行两个下角标值交换
"""
#导入包
from typing import List
#定义函数 函数名为removeDuplicates 传入列表和两个要进行值交换的下角标
def removeDuplicates(nums: List[int],index1,index2) -> int:
    #判断传入的两个下角标是否越界
    if index1<0 or index1>len(nums) or index2 < 0 or index2>len(nums):
        #如果越界 提示 索引越界
        raise Exception('索引越界')
    #否则
    else:
        #进行两个值交换
        nums[index1],nums[index2]=nums[index2],nums[index1]
    #返回交换值后的列表
    return nums
li=removeDuplicates([1,2,3,4],1,2)
print(li)