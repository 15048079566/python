"""
数组求并集（分离指针）
思路：确定最终数组的长度，确定主集合，将第二个集合中通过主集合下标的增长传值到主集合中
"""
#定义函数  函数名：mereTwo
def mereTwo(nums1,m,nums2,n):
    #i为下标 所以为m长度减1
    i = m - 1
    #j为下标 所以为n长度减1
    j = n - 1
    #k为数组的总长下标 所以为m+n-1
    k = m + n - 1
    while i >= 0 and j >= 0:
        #判断i下标值大于j下标值
        if nums1[i] >= nums2[j]:
            #将i下标值赋给k下标值
            nums1[k] = nums1[i]
            i -= 1
        else:
            #条件不成立时 将j下标的值赋给k下标值
            nums1[k] = nums2[j]
            j -= 1
        #赋给后 k要向前移动一位
        k -= 1
    #确保最后的集合中i下标的值全部传入最终集合中
    while i >= 0:
        #将i下标的值赋给k下标值
        nums1[k] = nums1[i]
        #i和k同时向前移动一步
        i -= 1
        k -= 1
    # 确保最后的集合中j下标的值全部传入最终集合中
    while j >= 0:
        # 将j下标的值赋给k下标值
        nums1[k] = nums2[j]
        #j和k同时向前移动一步
        j -= 1
        k -= 1
    #返回数组的并集
    return nums1
n = mereTwo([1,2,3,0,0,0],3,[-5,-4,-3],3)
print(n)


