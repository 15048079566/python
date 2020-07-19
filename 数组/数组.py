#数组类
class Arrary:
    #传入参数 capy代表一共可以传入多少个数据
    def __init__(self,capy):
        #建立None*capy个位置
        self.arrary=[None]*capy
        #初始大小为0
        self.size=0
    #插入函数 传入下角标和数据   index必须从0按顺序插入
    def insert(self,index,element):
        #判断index是否越界 不能够是负数 也不可能超过数据长度
        if index<0 or index>self.size:
            raise Exception('数组越界')
        #self.size添加数据就会+1 如果大于等于数据的总长 需要扩容 所以调用下面的addarrary函数 就是扩容函数
        if self.size>=len(self.arrary):
            self.addarrary()
        #遍历
        for i in range(self.size-1,index-1,-1):
            self.arrary[i+1]=self.arrary[i]
        #将新数据插入到总数据中
        self.arrary[index]=element
        #大小+1
        self.size+=1
    #扩容函数
    def addarrary(self):
        #新数组的长度为之前数组的2倍
        new_arrary=[None]*len(self.arrary)*2
        #遍历
        for i in range(self.size):
            #用过下角标将旧数据的值传给新数组
            new_arrary[i]=self.arrary[i]
        #再将新数组的值传回数组
        self.arrary=new_arrary
    #输出函数
    def output(self):
        #遍历
        for i in range(self.size):
            #打印每一个数据 用->连接
            print(self.arrary[i],end='->')
    #删除函数
    def pop(self,index):
        #判断要删除的数据的下角标是否越界
        if index < 0 or index>self.size:
            raise Exception('索引越界')
        #遍历 用传入的下角标开始到数据末尾
        for i in range(index,self.size):
            #将下角标为index后面的值向前移一步 覆盖掉index的值
            self.arrary[i]=self.arrary[i+1]
        #大小-1
        self.size-=1
if __name__ == '__main__':
    arrary=Arrary(4)
    for i in range(5):
        arrary.insert(i,i+1)
    arrary.output()
    for i in range(2):
        arrary.pop(0)
    print()
    arrary.output()
    # print(arrary)
