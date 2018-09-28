#coding=utf-8

"""
    归并排序.
    归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

    将数组分解最小之后，然后合并两个有序数组，
    基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
    然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

    递归思想.
"""


def mergeSort(list):
    n = len(list)
    #将列表进行递归拆分
    if n <= 1:
        return list
        # 列表只有一个元素的时候,直接返回该列表.
    mid = n//2
    llist = mergeSort(list[:mid])
    rlist = mergeSort(list[mid:])

    #     可以将rlist理解为归并排序后的右列表.
    #     可以将llist理解为归并排序后的左列表.
    #     定义2个指针,遍历需要归并的2个列表.
    left_point,right_point = 0,0
    #归并排序返回新的列表.
    result = []
    while left_point < len(llist) and right_point < len(rlist):
        if llist[left_point] > rlist[right_point]:
            result.append(rlist[right_point])
            right_point +=1
        else:
            result.append(llist[left_point])
            left_point +=1
    # 如果左右合并的时候,有一边已经append完了,就需要把剩下的全部append全部添加到result
    result += llist[left_point:]
    result += rlist[right_point:]
    return result

list = [54,26,93,17,77,31,44,55,20]
print(list)
ll = mergeSort(list)
print(list)
print(ll)





