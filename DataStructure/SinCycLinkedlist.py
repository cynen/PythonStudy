#coding=utf-8

#单向循环列表.
# 尾节点指向头结点.

class Node(object):
    '''
        Node节点包含主题数据,以及指向下一个元素的指针.
    '''
    def __init__(self,item=None):
        self.next = None #指向下一个元素
        self.item = item # 当前节点的ele


class SinCycLinkedlist(object):

    def __init__(self):
        self.__head = None;

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head is None;

    def length(self):
        '''返回链表的长度'''
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1;
        while cur.next != self.__head:
            count += 1;
            cur = cur.next;
        return count
    def add(self,item):
        '''在头部添加一个节点'''
        node = Node(item);
        if self.is_empty():
            # 空链表,就直接插入在头部.
            self.__head = node;
            node.next = self.__head;
        else: # 非空
            # 先将被添加的节点的next指向头节点.
            node.next = self.__head
            # 定义一个游标,指向头节点.
            cur = self.__head
            # 获取尾节点.
            while cur.next != self.__head:
                #找到尾节点
                cur = cur.next
            # 尾节点指向插入的元素.
            cur.next = node
            #插入头节点
            self.__head = node;
    def travel(self):
        '''遍历'''
        cur = self.__head
        if self.is_empty():
            return
        cur = self.__head;
        while cur.next != self.__head:
            print(cur.item,end="")
            cur = cur.next;
        print(cur.item) # 最后一个元素,没有打印出来.补打.
    """

    append(item)
    在尾部添加一个节点
    insert(pos, item)
    在指定位置pos添加节点
    remove(item)
    删除一个节点
    search(item)
    查找节点是否存在
    """



if __name__ == "__main__":

    sll = SinCycLinkedlist();
    sll.add(1);
    #print(sll.length())
    sll.travel();

    sll.add(2);
    sll.add(4);
    #print(sll.length())
    sll.travel();

