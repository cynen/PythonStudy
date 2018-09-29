#coding=utf-8



"""
    快速排序.
    又称划分交换排序（partition-exchange sort），
    通过一趟排序将要排序的数据分割成独立的两部分，
    其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，
    整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""


#
# list 需要排序的列表, start 排序起始索引. end 排序终止索引.
def quickSort(list,start,end):
    '''快排'''
    # if len(list) <= 1:
    #     return
    if start >= end:
        return


    mid_value = list[start]
    low = start
    high = end
    while low < high:
        # 由于取得中值是左边,应该先移动右边.(此顺序必须保证.)
        while low < high and list[high] >= mid_value :
            high -=1
        list[low] = list[high] # 因为此时,low索引上的数据还是midvalue,可以被更改!!!
        # 右边移动到比中值小的时候,就开始移动左边.
        while low < high and list[low] < mid_value:
            low +=1
        list[high] = list[low]
    #退出循环的时候,需要设置midvalue
    list[low] = mid_value

    # 快排左边.
    quickSort(list,start,low-1);
    # 快排右边.
    quickSort(list,low+1,end);


list = [54,26,93,17,77,31,44,55,20,37]
print(list)
quickSort(list,0,len(list)-1)
print(list)
