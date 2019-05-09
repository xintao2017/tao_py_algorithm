#!/usr/bin/env python

__author__ = "TAO XIN"
__copyright__ = "copyright: MIT License"

from decorators import timer

"""
 Merge sort function which sort a collection of numbers

 Merge sort:
  Worst case performance O(n log n)
  Best case performance O(n log n)
  Average case O(n log n)
"""

@timer
def merge_sort(iList):
    m_sort(iList)

def m_sort(iList):

    if len(iList) > 1:
        mid = len(iList) // 2

        L = iList[:mid]
        R = iList[mid:]

        m_sort(L)
        m_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                iList[k] = L[i]
                k += 1
                i += 1
            else:
                iList[k] = R[j]
                k += 1
                j += 1

        ## Check if any elements left in both L & R
        ## Append them to the end of iList

        while i < len(L):
            iList[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            iList[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    testList = [12, 45, 1, 23, 15, 69, 12, 23, 5,65, 99, 100, 78]

    merge_sort(testList)

    print(testList)
