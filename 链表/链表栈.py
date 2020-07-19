from typing import Any,Optional,NoReturn
#节点类
class Node:
    def __init__(self,data:Any,next:Optional=None):
        self.data=data
        self.next=next
    def __repr__(self):
        return f'Node({self.data})'
#链表栈类
class LinkerStack:
    def __init__(self):
        self.top=None
        self.size=0
#压栈 就是插入
    def push(self,item):
        node=Node(item)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.size+=1
#弹栈 就是删除
    def pop(self):
        if self.top is None:
            raise Exception('空表')
        else:
            node=self.top
            self.top=self.top.next
            self.size-=1
            return node.data
#判断是否为空
    def is_empty(self):
        return self.top is None
#栈顶 就是最后一项
    def peek(self):
        if self.top :
            return self.top
#重写
    def __repr__(self):
        curr=self.top
        string=''
        while curr:
            string +=f'{curr}-->'
            curr=curr.next
        return string +'END'
if __name__ == '__main__':
    li = LinkerStack()
    for i in range(10):
        li.push(i)
    print(li)
    # for i in range(5):
    #     li.pop()
    # print(li)
    print(li.is_empty())
    print(li.peek())
    print(li.size)

