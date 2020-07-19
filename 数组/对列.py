class Quece:  # 对列
    def __init__(self):
        self.entries = []  # 空值
        self.lenght = 0  # 字符长度
        self.front = 0  # 首位

    def __str__(self):
        # 【1：-1】把符号截取掉
        printed = '<' + str(self.entries)[1:-1] + '>'
        return printed
# 添加

    def put(self, item):
        self.entries.append(item)
        self.lenght += 1
# 删除

    def get(self):
        # 这是首项 返回出去 用return
        dequeue = self.entries[self.front]
        # 把后面的数据向前一步
        self.entries = self.entries[1:]
        # 长度-1
        self.lenght -= 1
        return dequeue
# 看首项

    def fron(self):
        return self.entries[0]
# 求长度

    def size(self):
        return self.lenght


if __name__ == '__main__':
    li = Quece()
    for i in range(10):
        li.put(i)
    print(li)
    for i in range(5):
        li.get()
    print(li)
    print(li.fron())
    print(li.size())
