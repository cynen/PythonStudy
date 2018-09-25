#coding=utf-8


class Queue(object):
    def __init__(self):
        self.__items=[]

    def enqueue(self,item):
        '''往队列中添加一个item元素'''
        self.__items.insert(0,item)
        #self.__items.append(item)

    def dequeue(self):
        '''从队列头部删除一个元素'''
        if self.size():
            return self.__items.pop() # 弹出第一个元素.
            #return self.__items.pop(0)  # 弹出第一个元素.
        else:
            return None;

    def is_empty(self):
        '''判断一个队列是否为空'''
        #return self.__items == []
        return not self.__items
    def size(self):
        '''返回队列的大小'''
        return len(self.__items)

if __name__=="__main__":
    q = Queue()
    print(q.size())
    print(q.is_empty())
    q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.size())
    print(q.is_empty())
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q.is_empty())



"""   def enqueue(self,item):
        '''往队列中添加一个item元素'''
        self.__items.append(item)

    def dequeue(self):
        '''从队列头部删除一个元素'''
        if self.size():
            return self.__items.pop(0) # 弹出第一个元素.
        else:
            return;
"""