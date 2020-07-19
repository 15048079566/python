from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.value=data
        self.left=None
        self.right=None
        self.parent=parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s"%(self.value):(self.left,self.right)},indent=1)
class BST:
    def __init__(self):
        self.root=None
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def __str__(self):
        return str(self.root)
    def is_right(self,node):
        return node==node.parent.right

    def __insert(self,value):
        new_node=Node(value,None)
        if self.is_empty():
            self.root=new_node
        else:
            parent_node=self.root
            while True:
                if value<parent_node.value:
                    if parent_node.left is None:
                        parent_node.left=new_node
                        break
                    else:
                        parent_node=parent_node.left
                elif value>=parent_node.value:
                    if parent_node.right is None:
                        parent_node.right=new_node
                        break
                    else:
                        parent_node=parent_node.right
            new_node.parent=parent_node
    def insert(self,*values):
        for value in values:
            self.__insert(value)
        return self
    def serch(self,value):
        if self.is_empty():
            print("空树")
        else:
            node=self.root
            while node and value !=node.value:
                if value<node.value:
                    node=node.left
                elif value>=node.value:
                    node=node.right
            print(node)
            return node
    def remove(self,value):
        search_node=self.serch(value)
        if search_node is not None:
            if search_node.left is None and search_node.right is None:
                self.__ressgin_nodes(search_node, None)
            elif search_node.left is None:
                self.__ressgin_nodes(search_node, search_node.right)
            elif search_node.right is None:
                self.__ressgin_nodes(search_node, search_node.left)
            else:
                tmp_node = self.get_max(search_node.left)
                self.remove(tmp_node.value)
                search_node.value = tmp_node.value
    def __ressgin_nodes(self,node,new_children):
        if new_children is not None:
            new_children.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=new_children
            else:
                node.parent.left=new_children
        else:
            self.root=new_children
    def get_max(self,node=None):
        if node is None:
            node=self.root
        if not self.is_empty():
            while node.right is not None:
                node=node.right
            return node
    def pre_order(self,node):
        if node is None:
            return
        print(node.value,end=',')
        self.pre_order(node.left)
        self.pre_order(node.right)
        return node
    def preorder(self,node):
        if node is None:
            return
        self.pre_order(node.left)
        print(node.value,end=",")
        self.pre_order(node.right)
        return node
    def pro_order(self,node):
        if node is None:
            return
        self.pro_order(node.left)
        self.pro_order(node.right)
        print(node.value,end=",")

if __name__ == '__main__':
    bst=BST().insert(8,3,6,10)
    print(bst)
    print('++++++++++++++++')
    # bst.remove(14)
    bst.pre_order(bst.root)
    print(bst)
    bst.preorder(bst.root)
    print(bst)
    bst.pro_order(bst.root)
    print(bst)