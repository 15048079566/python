"""
数组求交集（分离指针）
思路：先将数组进行排序 两个数组进行比较 相等时添加到一个新的数组中 在将新的数组进行有序不重复排列
"""
def intersection(nums1,nums2):
    nums1.sort()
    nums2.sort()
    i=0
    j=0
    nums_set=set()
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            nums_set.add(nums1[i])
            i+=1
            j+=1
    return list(nums_set)
li=intersection([4,9,5,3,6],[1,6,4,9])
print(li)