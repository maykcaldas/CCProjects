# -*- coding: utf-8 -*-
 
import os
import time
import random
#import numpy as np


def insertionSort(listToSort):
    ''' '''
    for i in range(1, len(listToSort)):
        currentPos = i
        checkPos = i-1
        while (listToSort[checkPos] > listToSort[checkPos+1]) and (checkPos >= 0):
            listToSort[checkPos], listToSort[checkPos+1] = listToSort[checkPos+1], listToSort[checkPos]
            checkPos -= 1
    return listToSort



def selectionSort(listToSort):
    '''
        The selection sort algorithm search the list len(list) times.
        At each search, it changes the position of the smaller element of the list with the current position of the search. 
    '''
    for i in range(len(listToSort)):
        minPos = i
        for j in range(i, len(listToSort)):
            if listToSort[j] < listToSort[minPos]:
                minPos = j
        listToSort[minPos], listToSort[i] = listToSort[i], listToSort[minPos]

    return listToSort
    
def mergeSort():
    pass


def bubbleSort():
    pass


def quickSort():
    pass



def heapSort():
    pass


def countingSort():
    pass


def main():

    sort = []

    for i in range(10000):
        sort.append(random.randint(0,5))

    sort1=sort[:]
    sort2=sort[:]

    # sort1=selectionSort(sort1)

    # sort1[300],sort1[500]=sort1[500],sort1[300]

    start=time.time()
    insertionSort(sort1)
    print("InsertionSort runned in ", time.time()-start)

    start=time.time()
    selectionSort(sort2)
    print("SelectionSort runned in ", time.time()-start)

main()
#os.system("pause")
