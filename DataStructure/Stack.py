#coding=utf-8


class Stack(object):

    def __init__(self):
        self.__list = [] #使用List实现Stack
    def push(self,item):
        '''添加一个新的元素item到栈顶'''
        self.__list.append(item)  # 将新的元素添加到尾部.

    def pop(self):
        '''弹出栈顶元素'''
        return self.__list.pop() # 弹出最后的一个元素.
    def peek(self):
        '''返回栈顶元素'''
        return self.__list[-1] #

    def is_empty(self):
        '''判断栈是否为空'''
        return not self.__list
    def size(self):
        '''返回栈的元素个数'''
        return  len(self.__list)

if __name__ == "__main__":
    s = Stack();
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print("Stack是否为空: "+str(s.is_empty()))
    print("元素个数: "+str(s.size()))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("Stack是否为空: "+str(s.is_empty()))
    print("元素个数: "+str(s.size()))
