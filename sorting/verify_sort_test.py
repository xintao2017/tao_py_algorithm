from quick_sort import quick_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from random import randint


def gen_a_big_list():

    alist = [randint(0, 1000) for x in range(0, 10000)]

    return alist


if __name__ == '__main__':

    iList = gen_a_big_list()

    #start = time.time()
    quick_sort(iList)
    #end = time.time()

    #print("Quick Sort Calculation time: {}".format(end-start))

    #start = time.time()
    merge_sort(iList)
    #end = time.time()

    #print("Merge Sort Calculation time: {}".format(end-start))

    #start = time.time()
    heap_sort(iList)
    #end = time.time()

    #print("Heap Sort Calculation time: {}".format(end-start))
