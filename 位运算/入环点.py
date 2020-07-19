"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
思路：使用快慢指针 让快指针一次移动两步 慢指针移动一步 当快指针和慢指针的节点为同一个节点时 说明链表有环 再让慢指针回到头部
快指针停留在他俩相同的节点上 通过循环让快慢指针每次移动一步 当他俩节点再次相等时 这个节点就是入环点
"""
#创建结点类 传入参数
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
#定义函数 函数名为detectCirclePoint
def detectCirclePoint(head):
    #快指针从头开始
    fast = head
    #慢指针也从头开始
    slow = head
    #循环 条件是快指针和快指针的下一节点不为空
    while fast and fast.next:
        #快指针每次移动两步
        fast = fast.next.next
        #慢指针每次移动一步
        slow = slow.next
        #当快指针和慢指针相等时  说明链表有环 接下来找入环点的位置
        if fast == slow:
            #将慢指针回到头部  找入环点
            slow = head
            #循环 找入环点
            while slow != fast:
                #慢指针每次移动一步
                slow = slow.next
                #快指针每次移动一步
                fast = fast.next
            #返回慢指针 这就是入环点
            return slow
    #如果快慢指针不相等 说明链表没有环 返回空
    return None
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4
    print('入环点为:%s'%(detectCirclePoint(node1)))
