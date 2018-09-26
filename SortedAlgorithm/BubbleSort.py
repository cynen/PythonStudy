#coding=utf-8



'''
    冒泡排序.
'''



def bubleSort2(list):
    for j in range(len(list)-1):  # 控制循环测次数,
        for i in range(len(list)-1): # 每循环遍历一遍,可以挑选出最大者,放到list末尾.(已经排好一位.)
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list


def bubleSort(list):
    '''优化后的'''
    for j in range(len(list)-1,0,-1): # 一共需要循环调用的次数.
        for i in range(j):
            # 下一次循环处理的元素个数比上一次递减1,最大值已经确定,并且至于list末尾.
            # 故,只需要比较剩余个数.
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


list = [33,66,22,77,99,11,55,44,88]
ll = bubleSort(list)
print(ll)








