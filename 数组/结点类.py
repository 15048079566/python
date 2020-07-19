class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
if __name__ == '__main__':
    no=Node(0)
    print(no)