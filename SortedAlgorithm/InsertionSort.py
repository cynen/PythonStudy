#coding=utf-8

"""
    插入排序:
    实现原理:
    1.构建一个有序的列表
    2.将待插入的元素和列表中元素比对,插入指定位置.

"""


def insertSort(list):
    #从第2个元素开始向前插入. 拿数进行和前面的数据比较.
    for i in range(1,len(list)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
    return list


############暂未实现.
def insertSort2(list):
    #从第2个元素开始向前插入. 拿数进行和前面的数据比较.
    for i in range(1,len(list)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,-1,-1):
            if list[i] < list[j]:
                list[j],list[i] = list[i],list[j]
    return list


list = [9,6,4,2,7,1,8]
ll = insertSort2(list)
print(ll)

print([i for i in range(5,-1,-1)])