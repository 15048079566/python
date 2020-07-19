"""
近似三数之和（对撞指针）
思路：循环 确定一个中心位数 用对撞指针求left和right的和 如果三个数之和不等于0 让中心位加一 以此类推
"""
from typing import List
def threeSum(nums:List,targat):
    #排序
    nums.sort()
    #给定一个最小值
    min=abs(nums[0]+nums[1]+nums[2]-targat)
    #结果
    res=nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        left=i+1
        right=len(nums)-1
        while left<right:
            #sum临时变量  为三个数之和
            sum=nums[i]+nums[left]+nums[right]
            #判断总和-指定值的绝对值是否小于最小值
            if abs(sum-targat)<min:
                #将总和-指定值的绝对值赋给最小值
                min=abs(sum-targat)
                #最后结果为sum
                res=sum
            #总和大于指定值
            if sum>targat:
                #右指针前移一步
                right-=1
            #总和小于指定值
            elif sum<targat:
                #左指针后移一步
                left+=1
            else:
                #相等时 返回sum
                return sum
    return res
li=threeSum([-1,2,0,-4],1)
print(li)