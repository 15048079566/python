"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
思路：取一个中间值 设置两种情况 一种是回文子串是奇数情况下 取一个中间值 判断中间值的两遍值是否相等 同时判断回文子串的长度
另一种情况就是回文子串是偶数的情况下 设想i和i+1是中间的两个值 这两个值相等 接着判断i-1和i+3是否相等 以此类推 在判断是奇数情况下返回回文子串
的长度和偶数情况下返回字符串的长度谁更加长 最长的就是最终结果返回最长的回文子串
"""
#定义函数 函数名为longesPalindroms
def longesPalindroms(strs):
    #length为字符串的长度
    length=len(strs)
    #如果这个字符串的长度小于2  说明只有一个值 所以直接返回就是最长的回文子串
    if length<2:
        #返回回文子串
        return strs
    #设置最大长度就是1
    maxlen=1
    #回文子串的初始值为第一个字符串
    res=strs[0]
    #遍历
    for i in range(length-1):
        #奇数情况下 调用centerSparead函数 传入字符串和参数
        odd=centerSparead(strs,i,i)
        #偶数情况下 调用centerSparead函数 传入字符串和参数
        even=centerSparead(strs,i,i+1)
        #如果奇数情况下的长度大于偶数情况下  讲回文子串传给maxstr临时变量
        maxstr=odd if len(odd)>len(even) else even
        #判断 传入字符串的长度大于最大字符串的长度吗？
        if len(maxstr)>maxlen:
            #传入的字符串长度大于最大字符串长度   将传入的字符串长度赋值最大字符串长度
            maxlen=len(maxstr)
            #将最长字符串传给res临时变量
            res=maxstr
    #返回最长回文子串
    return res
#定义函数 函数名为centerSparead  用于上方调用
def centerSparead(strs,left,right):
    #长度为字符串的总长
    length=len(strs)
    #赋值
    i=left
    j=right
    #循环条件 不能越界 用0开始 不能超过字符串总长
    while i>=0 and j < length:
        #判断 如果下标i和下标j对应的值相等
        if strs[i]==strs[j]:
            #下标i前移一步   为下一个判断
            i-=1
            #下标j后移一步  为下一判断
            j+=1
        else:
            #条件不成立 直接跳出循环
            break
    #返回符合条件的回文子串
    return strs[i+1:j]
print(longesPalindroms("e,a,b,c,d,c,b,a"))
