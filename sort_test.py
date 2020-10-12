'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
@File  :sort_test.py
@Author:wufeitong 公众号「吾非同」
@Date  :2020/10/12
'''

# 1.冒泡排序
def bubble_sort(aList):
    n = len(aList)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)


# 2.选择排序
# 选择排序是每次找出最小的索引，然后替换数据的位置


def select_sort(aList):
    l = len(aList)

    for j in range(l):
        min_index = j
        for i in range(min_index + 1, l):
            if aList[min_index] > aList[i]:
                min_index = i
        # 循环一遍后找到最小的索引
        aList[j], aList[min_index] = aList[min_index], aList[j]


if __name__ == "__main__":
    li = [9, 16, 17, 15, 11]
    print(li)
    select_sort(li)
    print(li)

# 3.插入排序
def insert_sort(aList):
    '''插入排序'''
    n = len(aList)
    for i in range(n):
        j = i
        # print('j= ', j)
        while j > 0:
            if aList[j] < aList[j - 1]:
                aList[j], aList[j - 1] = aList[j - 1], aList[j]
            # print(j)
            j -= 1
        # print(' ')


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)