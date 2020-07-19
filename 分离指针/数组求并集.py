"""
数组求并集（分离指针）
思路：确定最终数组的长度，确定主集合，将第二个集合中通过主集合下标的增长传值到主集合中
"""
def mereTwo(nums1,m,nums2,n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1
n = mereTwo([1,2,3,0,0,0],3,[-5,-4,-3],3)
print(n)


