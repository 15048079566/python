"""
三数之和（对撞指针）
思路：循环 确定一个中心位数 用对撞指针求left和right的和 如果两个数之和没有符合条件 让中心位加一 以此类推
"""
#导入包
from typing import List
#定义函数 函数名位nums
def threeSum(nums:List):
    #将列表排序
    nums.sort()
    #新建一个空列表
    result=[]
    #中心位
    for i in range(len(nums)-2):
        if i >0 and nums[i]==nums[i-1]:
            continue
        #左指针为i+1
        left=i+1
        #右指针为列表总长减1
        right=len(nums)-1
        #循环条件 左指针小于右指针
        while left<right:
            #中心位数+左指针值+右指针大于0
            if nums[i]+nums[left]+nums[right]>0:
                #右指针前移一步
                right-=1
            # 中心位数+左指针值+右指针小于0
            elif nums[i]+nums[left]+nums[right]<0:
                #左指针后移一步
                left+=1
            #否则
            else:
                #将值添加到result列表中
                result.append([nums[i], nums[left], nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-1
                left+=1
                right-=1
        return result
li=threeSum([-1,0,2,1,3,0,-2])
print(li)
