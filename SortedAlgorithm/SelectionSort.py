#coding=utf-8



"""
    选择排序:
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，
    然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

    重点关注 尾部未排序的元素.
"""


def selectionSort(list):
    '''
    选择排序
    :param list:
    :return: list
    '''
    for i in range(len(list)): # 遍历当前列表的每个元素
        #
        # 假设当前i索引位置的元素值最小. 标记min_index
        # 使用当前的list[i] 去和i索引后面的元素进行比较.
        # 如果list[i] 大于后面的某个元素, 就更改 游标位置为当前较小值得索引 j
        # 一次循环完成后,比较min_index和i是否一致.不一致就交换数据.
        # 记录索引.
        min_index = i # 最小值的索引
        for j in range(i+1,len(list)): # [i+1,len) j in [i+1,i+2,...]
            if list[j] < list[min_index]:
                min_index = j # 当前元素比假设最小值还小.
        if min_index != i: # 如果当前最小值的索引不是i,就需要交换数据.
            list[i],list[min_index] = list[min_index],list[i]
    return list




list = [33,66,22,77,99,11,55,44,88]
ll = selectionSort(list)
print(ll)
