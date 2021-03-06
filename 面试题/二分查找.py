"""
二分查找（对撞指针）
思路：定义两个指针left和right指针 判断指定值大于中间值 如果大于那就把中间值赋给left指针 如果小于中间值  就把中间值赋给right指针 以此类推
"""
#定义函数 函数名为binarySearch
def binarySearch(nums:list,val):
    #lest指针初始值为-1
    left=-1
    #right初始值为数组总长+1
    right=len(nums)
    #循环
    while left<=right:
        #如果指定值不在数组中 返回-1
        if val not in nums:
            return -1
        #取中间值
        mid=left+(right-left)//2
        # 指定值大于中间值 把中间值赋给left指针
        if val>nums[mid]:
            left=mid
        #指定值小于中间值 把中间值赋给right指针
        elif val<nums[mid]:
            right=mid
        #否则 返回中间值 说明指定值就是中间值
        else:
            return mid

b=binarySearch(list(range(10)),5)
print(b)

"""
二分查找（递归版）
思路：调用函数 定义两个指针left和right指针 判断指定值大于中间值 如果大于那就把中间值赋给left指针 如果小于中间值  就把中间值赋给right指针 以此类推
"""
##定义函数 函数名为 binarySearch
# def binarySearch(nums,target,left,right):
#     if right>0:
#         #取中间值 优化版 适用所有编程
#         mid=left+(right-left)//2
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]>target:
#             return binarySearch(nums,target,left,mid-1)
#         else:
#             return binarySearch(nums,target,mid+1,right)
#     else:
#         return -1
# b=binarySearch(list(range(10)),1,-1,11)
# print(b)
