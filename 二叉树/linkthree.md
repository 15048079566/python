### 二叉树的创建和查询
    创建二叉树首先要创建一个根，在根再分为两个子叶，分别是左子叶和右子叶， 同时如果还有子叶，那么左右子叶为新添加子叶的
    根 根据下图理解 数字代表创建树的顺序
       1           1            1                  1     
                  /  \         /  \               /  \ 
                              2     3            2     3    ....
                             /  \  / \          /  \  / \
                                               4   5 6   7
### 创建结点类
    class Node:   
        def __init__(self, data):
            表示对应的元素
            self.data = data  
            表示左节点
            self.left = None  
            表示右节点
            self.right = None  
        
        格式化输出
        def __repr__(self):   
            return f"Node({self.data})"
### 创建树        
    class Tree:     
        def __init__(self):
        链表的头结点定义为根节点 root
            self.root = None   
          
        创建树 添加根和子叶
        def add(self, item):
            临时变量node接收插入数   
            node = Node(item)
            如果二叉树为空，那么生成的二叉树最终为新插入树的点
            if self.root is None:  
                self.root = node
            else:
                temp是列表 列表中的数据就是根节点 每次添加的节点用于下次循环
                temp = [self.root]  
                循环
                while True:
                    节点为根节点 列表中的初始值为根 符合条件添加到列表中
                    pop_node = temp.pop(0)
                    左子树为空则将点添加到左子树
                    if pop_node.left is None:  
                        pop_node.left = node
                        return
                    右子树为空则将点添加到右子树
                    elif pop_node.right is None:  
                        pop_node.right = node
                        return
                    else:
                        否则将根节点的左右子树添加到列表中 用于下次循环 
                        temp.append(pop_node.left)
                        temp.append(pop_node.right)
####         
    查询父节点也就是子树的根节点：（只返回符合条件的第一个查询的结果）新建一个根节点 判断父节点的值是否和传入的值相等 如
    果相等 返回None 因为根节点没有父节点 如果根节点的值不相等在查找根节点的左右子树 如果左右子树的其中一个值等于传入的值
    说明根节点就是传入值的父节点,如果没有符合条件的就把左右子树添加到列表中 进行循环 也就是说传入的左右子树 就是用于下次
    循环的父节点，道理就像查找家族人员的名字 爷爷是父节点 爸爸是子树 再往下找的话 爸爸就是父节点 儿子就是子树以次类推 如
    果没有找到结果 就返回None  
####
        def get_parent(self, item):
            if self.root.data == item:
            根节点没有父节点
                return None  
            临时列表用于存放根节点
            temp = [self.root]
            循环
            while temp:
                传入根节点
                pop_node = temp.pop(0)
                某节点的左子树为寻找的点
                if pop_node.left.data == item:  
                    返回某节点，即为寻找点的父节点
                    return pop_node  
                某节点的右子树为寻找的点
                if pop_node.right.data == item:  
                    返回某节点，即为寻找点的父节点
                    return pop_node  
                if pop_node.left:  
                    添加到临时列表temp
                    temp.append(pop_node.left)
                if pop_node.right:
                    temp.append(pop_node.right)
            return None
    
####
    查询父节点（可以返回符合条件的多个结果） 和上方查询时方式是一样的知识在添加
    到列表中把左右子树同时传入列表 即使左子树的条件符合了返回值 但是列表中还有右
    子树的值 需要把列表中的值全部删除循环才停止 所以可以返回多个符合条件的结果
####
        def get_parent1(self, item):
            根节点的值和传入的值相等时 返回None 根节点没有父节点
            if self.root.data == item:
                return None
            用于存放最终结果
            res = []
            存放子树
            temp = [self.root]
            while temp:
                pop_node = temp.pop(0)
                根节点的左节点不为空 并且左子树的值等于传入的值 说明此时就是父节点
                if pop_node.left and (pop_node.left.data == item):
                    res.append(pop_node)
                符合条件的添加到最后结果列表res中
                elif pop_node.right and (pop_node.right.data == item):
                    res.append(pop_node)
                如果当前结点有左结点,收集起来待遍历
                if pop_node.left: 
                    temp.append(pop_node.left)
                if pop_node.right:  
                    如果当前结点有右节点,收集起来待遍历
                    temp.append(pop_node.right)
            return res    
            
#### 验证：       
    if __name__ == '__main__':
        tree = Tree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        tree.add(5)
        tree.add(7)
        print(tree.root.left.left)
        print(tree.root.left.right)
        print(tree.get_parent(5))
        print(tree.get_parent1(5))
        print(tree.root.left.right)
#### 结果：
    Node(4)
    Node(5)
    Node(2)
    [Node(2), Node(3)]
    Node(5)


