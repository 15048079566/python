"""
数组求交集（分离指针）
思路：先将数组进行排序 两个数组进行比较 相等时添加到一个新的数组中 在将新的数组进行有序不重复排列
"""
#定义函数 函数名intersection 传入两个数组
def intersection(nums1,nums2):
    #将数组排序
    nums1.sort()
    nums2.sort()
    i=0
    j=0
    #用于接收最终结果的集合 进行有序不重复
    nums_set=set()
    #先排序 然后两个数组谁小谁+1
    while i<len(nums1) and j<len(nums2):
        #判断i指针的值小于j指针的值
        if nums1[i]<nums2[j]:
            #i指针向后移一步
            i+=1
        #i指针的值大于j指针的值
        elif nums1[i]>nums2[j]:
            #j指针向后移一步
            j+=1
        #否则
        else:
            #添加到列表中
            nums_set.add(nums1[i])
            #两个指针同时后移一步
            i+=1
            j+=1
    #返回最终列表
    return list(nums_set)
li=intersection([4,9,5,3,6],[1,6,4,9])
print(li)