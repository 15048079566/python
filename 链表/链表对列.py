from typing import Any,Optional
#新建结点类
class Node:
    #插入参数
    def __init__(self,data:Any,next:Optional=None):
        self.data=data
        self.next=next
    #重写
    def __repr__(self):
        return f'Node({self.data})'
#新建对列
class Queue:


    def __init__(self):
        #首相为空
        self.frond=None
        #尾项为空
        self.rear=None
        #长度大小为0
        self.size=0
    #插入，对列在尾部插入
    def psh(self,item):
        #新数据
        node=Node(item)
        #判断数据是不是为空值
        if self.frond is None:
            #是空值时直接插入
            self.frond=node
            self.rear=node
        else:
            #尾部的下一项就是新数据
            self.rear.next=node
            #重新定义尾项
            self.rear=node
        #添加一个数据时 长度大小增加1
        self.size+=1
    #删除数据 从首相开始删除
    def pop(self):
        #判断起始数据是不是为空 如果为空返回这是空链表
        if self.frond is None:
            raise Exception('空链表')
        else:
            #否则情况下 要删除的数据为首相
            node=self.frond
            #首相等于首相的下一项 相当于数据覆盖 数据向前移
            self.frond=node.next
        #删除一个 数据长度大小-1
        self.size-=1
        #返回删除数据
        return node.data
    #通过下角标查询数据
    def get(self,index):
        #先判断index有没有越界
        if index<0 or index>self.size:
            raise Exception('索引越界')
        else:
            #curr为一个临时变量
            curr=self.frond
            #循环  循环次数为下角标次数
            for i in range(index):
                curr=curr.next
        return curr
    #判断有没有数据
    def is_empty(self):
        return self.frond is None
    #判断数据长度大小
    def size(self):
        return self.size
    #重写
    def __repr__(self):
        curr=self.frond
        string=''
        while curr:
            string+=f'{curr}<--'
            curr=curr.next
        return string +'END'
if __name__ == '__main__':
    q=Queue()
    for i in range(5):
        q.psh(i)
    print(q)
    for i in range(2):
        q.pop()
    print(q)
    print(q.is_empty())
    print(q.size)
    print(q.get(2))
    print(q.pop())