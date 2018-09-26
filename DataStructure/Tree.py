

class Node(object):
    def __init__(self,item):
        self.item = item;
        self.lchild = None;
        self.rchild = None;




class Tree(object):
    '''Tree 的python实现.'''
    def __init__(self):
        '''定义一个根节点.'''
        self.root = None

    def add(self,item):
        '''向树中添加元素.
            使用广度优先策略.
            广度优先策略:确保每一层,都是满二叉树.否则从左向右补齐.
        '''
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root] #使用队列实现树.
        while queue: # 只有当前节点不为空,就会一直进行遍历.
            rootnode = queue.pop(0) # 获得当前树的root节点
            ########## 方法一 #################
            # if rootnode.lchild is None :
            #     rootnode.lchild = node
            #     return
            # else:
            #     queue.append(rootnode.lchild)
            # if rootnode.rchild is None:
            #     rootnode.rchild = node
            #     return
            # else:
            #     queue.append(rootnode.rchild)

            ########### 方法二 ################
            if rootnode.lchild is None: #当前节点的左孩子为空,就添加
                rootnode.lchild = node
                return
            elif rootnode.rchild is None: #否则,右孩子为空,就添加.
                rootnode.rchild = node
                return
            else: #左右孩子都不为空,就添加到队列中,准备解析.
                queue.append(rootnode.lchild)
                queue.append(rootnode.rchild)


    def travle(self):
        '''广度优先遍历'''
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.item,end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)


    def pretravel(self,node):
        '''先序遍历   根 -->左--> 右'''
        if node is None:
            return
        print(node.item,end=" ")
        self.pretravel(node.lchild)
        self.pretravel(node.rchild)

    def midtravel(self,node):
        '''中序遍历  左-->根-->右'''
        if node is None:
            return
        # if root.lchild is not None:
        self.midtravel(node.lchild)
        print(node.item,end=" ")
        # if root.rchild is not None:
        self.midtravel(node.rchild)

    def lastravel(self,node):
        '''后序遍历  左-->右-->根'''
        if node is None:
            return
        self.lastravel(node.lchild)
        self.lastravel(node.rchild)
        print(node.item,end=" ")

if __name__ == "__main__":
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    #      1
    #   2   3
    # 4  5 6  7
    t.travle()  # 广度优先.
    print("")
    t.pretravel(t.root)
    print("")
    t.midtravel(t.root)
    print("")
    t.lastravel(t.root)
    print("")
