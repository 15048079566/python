def fib(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return fib(n-1)+fib(n-2)
f=fib(5)
print(f)
"""青蛙跳台阶 第一次  第二次   第三次  第四次  第五次     第六次   第七次  第八次  ……  第n次
             1       2         3       5       8       13       21       34     （n-1）+（n-2）
              
              结论：n=1 return 1
                    n=2 return 2
                    n>2 return (n-1)+(n-2)1
              """