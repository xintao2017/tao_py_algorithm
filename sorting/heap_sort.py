
__author__ = "TAO XIN"
__copyright__ = "MIT License"

""" Heap sorting algorithm implementation!"""


def heapify(iList, n, i):
    # Initialize largest as root
    largest = i

    # Set left and right elements
    l = 2 * i + 1
    r = 2 * i + 2

    # Check if left element exist and larger than root
    if l < n and iList[i] < iList[l]:
        largest = l

    # Check if right element exist and larger than root
    if r < n and iList[largest] < iList[r]:
        largest = r

    # Check if largest has changed
    if largest != i:
        iList[i], iList[largest] = iList[largest], iList[i]
        # Heapify the root
        heapify(iList, n, largest)



def heap_sort(iList):
    n = len(iList)

    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(iList, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        iList[i], iList[0] = iList[0], iList[i]
        heapify(iList, i, 0)


if __name__ == '__main__':
    testList = [12, 45, 1, 23, 15, 69, 12, 23, 5,65, 99, 100, 78]

    heap_sort(testList)

    print(testList)
