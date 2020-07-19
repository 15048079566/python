#栈类
class Stack:
    def __init__(self,limit=10):
        self.stack=[]
        self.size=0
    def __str__(self):
        return str(self.stack)
#插入栈
    def push(self,data):
        self.stack.append(data)
        self.size+=1
#删除栈  从栈顶开始删除 栈顶就是最后一个插入的数据
    def pop(self):
        if self.stack is not None:
            self.stack.pop()
            self.size-=1
#栈顶
    def peek(self):
        if self.stack:
            return self.stack[-1]
#判断是否有数据
    def is_empty(self):
        return self.stack is None
#查看有多少数据
    def size(self):
        return self.size
if __name__ == '__main__':
    stack=Stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    for i in range(5):
        stack.pop()
    print(stack)
    print(stack.is_empty())
    print(stack.size)
    print(stack.peek())