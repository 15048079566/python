"""
14 编写一个函数来查找字符串数组中的最长公共前缀。
链接：https://leetcode-cn.com/problems/longest-common-prefix

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""

# a = [1, 2, 3]
# b = [4, 5, 6]
# #压缩
# zipped = list(zip(a, b))
# print(zipped)
# #遍历
# for each in zipped:
#     print(each)
# #解压
# for each in zip(*zipped):
#     print(each)
#
# strs = ["flower", "flow", "flight"]
# minLength = min([len(s) for s in strs])
# print(minLength)

from typing import List
#定义函数 函数名为longestCommonPrefix
def longestCommonPrefix(strs: List[str]):
    #判断传入的列表是不是空列表
    if len(strs) == 0 or "" in strs:
        return ""
    #当列表中只有一个字符串 直接返回这个字符串
    if len(strs) == 1:
        return strs
    #遍历列表每一个值 判断每一个字符串的长度 返回最短字符串长度
    minLength = min([len(s) for s in strs])
    #新建一个列表
    publicWord = []
    #遍历最短字符串长度
    for i in range(minLength):
        #遍历列表  ——> flower   flow  flight
        for word in strs:
            #添加到列表中   第一次循环‘f’二‘f’三 ‘f’ 第二次循环就是三个‘fl’ 第三次循环‘flo’‘flo’‘fli’
            publicWord.append(word[:i+1])
        #对新建的列表进行有序不重复排序  判断排序后长度是不是为1   第一次和第二次len都是1 第三次就是2
        if len(set(publicWord)) == 1:
            #清空列表
            publicWord = []
        #条件不满足时 返回strs切片
        else:
            #返回第一个值的就行 因为前面都是一样的
            return strs[0][:i]

# ["flower", "flow", "flight"]
#定义函数 函数名为longCommonPrefix
def longCommonPrefix(strs: List[str]):
    #空字符串
    res = ''
    #解压 遍历列表中字符串第一个值  接下来是第二个值 直到最短长度停止
    for each in zip(*strs):   #-->'f' 'f' 'f'----->'l' 'l' 'l'----->'o' 'o' 'i'
        #进行有序不重复排序 判断长度
        if len(set(each)) == 1:
            #满足就添加到字符串中
            res += each[0]
        else:
        #不满足条件返回字符串
            return res
    return res
#
#
if __name__ == '__main__':
    l = ["flower", "flow", "flight"]
    print(longCommonPrefix(l))
    print(longestCommonPrefix(l))

# strs=["flower", "flow", "flight"]
# for each in zip(*strs):
#     print(each)