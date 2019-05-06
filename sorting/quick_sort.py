#!/usr/bin/env python

__author__ = "TAO XIN"
__copyright__ = "copyright: MIT License"

"""
 A simple quick sort function which sort a collection of numbers

 Quick sort:
  Worst case performance O(n2)
  Best case performance O(n log n) or O(n)
  Average case O(n log n)
"""

def quick_sort(iList, low, high):
    if low < high:
        i = partition(iList, low, high)

        quick_sort(iList, low, i - 1)
        quick_sort(iList, i + 1, high)


def partition(iList, low, high):

    pivot = iList[high]

    i = low - 1

    for j in range(low, high):
        if iList[j] <= pivot:
            i += 1
            iList[i], iList[j] = iList[j], iList[i]
    iList[i+1], iList[high] = iList[high], iList[i+1]
    return i + 1


if __name__ == '__main__':
    testList = [12, 45, 1, 23, 15, 69, 12, 23, 5,65, 99, 100, 78]

    quick_sort(testList, 0, len(testList) - 1)

    print(testList)
