#coding=utf-8

"""
    希尔排序.
    希尔排序的基本思想是：
    将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。
    最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

"""






def shellSort(list):
    #希尔排序使用了插入算法.
    # 步长: gap
    gap = len(list)//2; # 设置步长.

    #gap 变化到0之前,插入算法执行的次数.
    while gap > 0:
        #插入算法,与普通的插入算法的区别就是gap步长.
        for i in range(gap,len(list)):
            # j = [gap,gap+1,gap+2,....]
            j = i;
            # while j > 0:
            #     if list[j] < list[j-gap]:
            #         list[j],list[j-gap] = list[j-gap],list[j]
            #         j -= gap
            #     else:
            #         break
            while j > 0 and list[j] < list[j-gap]:
                    list[j],list[j-gap] = list[j-gap],list[j]
                    j -= gap
        # 每次gap遍历完一次,需要重置一下gap值,压缩一半.
        gap //= 2

list = [9,6,4,2,7,1,8]
print(list)
shellSort(list)
print(list)