#导入包
from typing import List
#结点类
class Node:
    #传入参数
    def __init__(self,data):
        self.data=data
        self.next=None
    #重写
    def __repr__(self):
        return f'Node({self.data})'
#链表类
class LinkList:
    def __init__(self):
        #头部为空
        self.head=None
    #插入头部
    def insert_head(self,data):
        #新数据就是新的头部
        new_head=Node(data)
        #如果链表有数据
        if self.head is not None:
            #新节点的下一步指向头部
            new_head.next=self.head
        # 所以新节点就是头部
        self.head=new_head
    #重写
    def __repr__(self):
        #变量curr
        curr=self.head
        #空字符串
        string=''
        while curr:
            string+=f'{curr}-->'
            curr=curr.next
        return string + 'END'
    #输出函数
    def print_list(self):
        #临时变量temp
        temp=self.head
        while temp:
            #循环直接打印
            print(temp.data)
            temp=temp.next
    #在尾部插入数据
    def append(self,data):
        #如果链表为空 直接添加新数据为头
        if self.head is None:
            self.insert_head(data)
        else:
            #临时变量temp
            temp=self.head
            #循环到总数据的下一项
            while temp.next:
                temp=temp.next
            # 总数据的下一项为插入的新数据
            temp.next=Node(data)
    #在中间插入 传入插入数据的位置和数据
    def insert(self,i,data):
        #如果没有头 或者传入的i为1 那就为数据的头 第一项
        if self.head is None or i==1:
            self.insert_head(data)
        else:
            #new_node为传入的数据
            new_node=Node(data)
            #用快慢指针方法插入
            curr=self.head
            pre=curr
            j=1
            while j<i:
                pre=curr
                curr=curr.next
                j+=1
            #慢指针的下一项指向新数据
            pre.next=new_node
            #新数据的下一项指向快指针
            new_node.next=curr
    #直接表链接多元表 obj：传入的参数为列表
    def linklist(self,obj:List):
        #新数据为链表的第一个数值
        new_node=Node(obj[0])
        #头为新新数据
        self.head=new_node
        #curr临时变量
        curr=self.head
        #遍历obj的第二项
        for i in obj[1:]:
            curr.next=Node(i)
            curr=curr.next
    #删除头部
    def delete_head(self):
        if self.head is None:
            print('空链表')
        else:
            self.head=self.head.next
    #删除尾部
    def pop(self):
        curr=self.head
        if self.head is None:
            print('空链表')
        else:
            curr=self.head
            while curr.next.next:
                curr=curr.next
            curr.next=None
        return curr.next
    #删除尾部 快慢指针
    def delete_tail(self):
        curr=self.head
        pre=self.head
        if self.head is None:
            print('空链表')
        else:
            while curr.next:
                pre=curr
                curr=curr.next
            pre.next=None
if __name__ == '__main__':
    li=LinkList()
    li.insert_head(100)
    li.insert_head(90)
    li.insert(2,98)
    li.insert(3,99)
    li.delete_tail()
    print(li)

