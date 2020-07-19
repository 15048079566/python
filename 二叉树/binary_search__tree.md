#### 导入包
    from pprint import pformat
#### 创建节点
    class Node:
        def __init__(self,data,parent):
            传入数据
            self.value=data
            左子树
            self.left=None
            右子树
            self.right=None
            父节点
            self.parent=parent
         格式化输出
        def __repr__(self):
            左子树和右子树为空
            if self.left is None and self.right is None:
                返回传入参数
                return str(self.value)
            输出格式 间距为1
            return pformat({"%s"%(self.value):(self.left,self.right)},indent=1)
#### 创建BST
    class BST:
        def __init__(self):
            根节点
            self.root=None
        def __str__(self):
            以字符串格式返回根节点
            return str(self.root)
#### 判断根节点是否为空
        def is_empty(self):
            if self.root is None:
                return True
            return False
#### 判断节点为父节点的右子树值
        def is_right(self,node):
            返回此节点是不是父节点的右子树
            return node==node.parent.right
#### 私有函数插入
    def __insert(self,value):
        new_node=Node(value,None)
        判断根节点是不是为空
        if self.is_empty(): 
            根节点为新添加的结点     
            self.root=new_node   
        else:
            parent_node=self.root
            while True:
                传入的值和根节点的值进行对比 小于根节点的值 添加到左叶
                if value<parent_node.value:
                    判断左叶是不是含有数据   
                    if parent_node.left is None:
                        将传入的数据赋给左叶  
                        parent_node.left=new_node
                        跳出循环   
                        break  
                     左叶还有数据                     
                    else:   
                        就把左叶结点变为跟结点 进行下次循环                        
                        parent_node=parent_node.left 
                 添加到右叶 
                elif value>=parent_node.value: 
                    右叶是没有数据的时候   
                    if parent_node.right is None: 
                        把数据传给右叶  
                        parent_node.right=new_node  
                        跳出循环  
                        break
                    else:
                        右叶变为跟 进行下次循环
                        parent_node=parent_node.right  
            结点的父级就是左右叶 根据上面循环进行改变 所以才能在继续循环
            new_node.parent=parent_node  
#### 定义插入函数 *不定长字节
    def insert(self,*values):
        for value in values:
            #调用私有函数
            self.__insert(value)
        return self
#### 查询
    def serch(self,value):
        根节点为空时 
        if self.is_empty():
            print("空树")
        else:
            node=self.root
            while node and value !=node.value:
                 传入的值小于根节点的值 根节点为根节点的左叶
                if value<node.value:
                    node=node.left
                  传入的值大于等于根节点 根节点为根节点的右叶
                elif value>=node.value:
                    node=node.right
             打印
            print(node)
            return node
#### 删除节点
    （如果删除的节点没有子叶直接删除就可以，如果只有左子叶只要把节点替换成左子叶，如果只有右子叶只要把节点替换为右子叶
    如果左右子叶都存在时 需要找到左子叶的最大值或者是右子叶的最小值进行替换就可以）
####
    def remove(self,value):
        调用查询函数 查找到要删除节点的位置
        search_node=self.serch(value)
        
        if search_node is not None:
            没有孩子节点的情况
            if search_node.left is None and search_node.right is None:
                交换当前节点和None->当前节点变成空  
                self.__ressgin_nodes(search_node, None)  
            只有右侧孩子节点
            elif search_node.left is None: 
                self.__ressgin_nodes(search_node, search_node.right)  
            只有左侧孩子节点
            elif search_node.right is None:  
                self.__ressgin_nodes(search_node, search_node.left)
            左右孩子结点都有
            else: 
                找到左子树的最大结点 
                tmp_node = self.get_max(search_node.left) 
                删除节点 
                self.remove(tmp_node.value) 
                不改变树结构,只更改当前节点的值 
                search_node.value = tmp_node.value  
#### 私有函数 把要删除的节点进行替换
    def __ressgin_nodes(self,node,new_children):
        新孩子不是None
        if new_children is not None:
            节点的父节点为新节点的父节点  就是删除节点的子叶替换了要删除的节点
            new_children.parent=node.parent
        节点的父节点不是空
        if node.parent is not None:
            此节点为父节点的右子叶
            if self.is_right(node):
                新孩子为节点的父节点的右子叶
                node.parent.right=new_children
            else:
                新孩子为节点的父节点的左子叶
                node.parent.left=new_children
        else:
        否则新孩子为根节点
            self.root=new_children
#### 查找子叶的最大值
    def get_max(self,node=None):
        节点为空 返回根节点
        if node is None:
            node=self.root
        根节点不为空
        if not self.is_empty():
            节点的右子叶不为空
            while node.right is not None:
                查找节点的右子叶  查找到最后就是节点的左子叶的最大值
                node=node.right
            return node
#### 前序遍历（中左右）
    def pre_order(self,node):
        if node is None:
            return
        print(node.value,end=',')
        self.pre_order(node.left)
        self.pre_order(node.right)
        return node
#### 前序遍历图片连接
    https://imgchr.com/i/NzJcs1
#### 中序遍历（左中右）
    def preorder(self,node):
        if node is None:
            return
        self.pre_order(node.left)
        print(node.value,end=",")
        self.pre_order(node.right)
        return node
#### 中序遍历图片地址
    https://imgchr.com/i/NzJ6MR
#### 后序遍历（左右中）
    def pro_order(self,node):
        if node is None:
            return
        self.pro_order(node.left)
        self.pro_order(node.right)
        print(node.value,end=",")
#### 后序遍历图片地址
    https://imgchr.com/i/NzJgqx
#### 验证
    if __name__ == '__main__':
        bst=BST().insert(8,3,6,10)
        # print(bst)
        print('++++++++++++++++')
        # bst.remove(14)
        bst.pre_order(bst.root)
        print(bst)
        bst.preorder(bst.root)
        print(bst)
        bst.pro_order(bst.root)
        print(bst)
#### 结果
    {'8': ({'3': (None, 6)}, 10)}
    ++++++++++++++++
    8,3,6,10,{'8': ({'3': (None, 6)}, 10)}
    3,6,8,10,{'8': ({'3': (None, 6)}, 10)}
    6,3,10,8,{'8': ({'3': (None, 6)}, 10)}