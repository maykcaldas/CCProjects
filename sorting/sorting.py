# -*- coding: utf-8 -*-
 
import os
import time
import random
import matplotlib
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

def bubbleSort(listToSort):
    for i in range(len(listToSort)-1):
        for j in range(len(listToSort)-1-i):
            currentPos = j
            if listToSort[currentPos] > listToSort[currentPos+1]:
                listToSort[currentPos], listToSort[currentPos+1] = listToSort[currentPos+1], listToSort[currentPos]
    
    return listToSort

def mergeSort(listToSort):
    ''' '''
    # def divide(listToSort):
    #     if len(listToSort) > 1:
    #         return listToSort, []
    #     else:
    #         return listToSort[:len(listToSort)/2], listToSort[len(listToSort)/2:]

    def divide(listToSort):
        ret=[]
        for i in listToSort:
            ret.append([i])

        return ret

    def merge(listToSort):

        ret=[]
        while(len(listA)!=0 or len(listB)!= 0):
            if len(listA)!=0 and len(listB)!=0:
                a=listA.pop()
                b=listB.pop()
            
                if a > b:
                    ret.append(a)
                else:
                    ret.append(b)
            elif len(listA)!=0 and len(listB)==0:
                ret.append(a)

            elif len(listB)==0 and len(listB)!=0:
                ret.append(b)
        return ret

    listToSort=divide(listToSort)
    listToSort=merge()

    return listToSort

def heapSort():
    pass


def quickSort():
    pass



def countingSort():
    pass


def shellSort():
    pass

def timeTest(listToSort, func, name="The test"):
    start=time.time()
    func(listToSort)
    print("{0:15s} runned in {1:15.10f} s".format(name, time.time()-start))

def main():

    sort = []
    # sort = [1,4,56,6,1,4,56,7,54,25,67,7,5,4,3,5,7,89,-8,0,0,98,867,5,2,3,123]
    # print(sort)

    for i in range(10000):
        sort.append(random.randint(0,10000))

    # sort=selectionSort(sort)
    # sort[300],sort[500]=sort[500],sort[300]

    sort1=sort[:]
    sort2=sort[:]
    sort3=sort[:]
    sort4=sort[:]

    # print(mergeSort(sort))

    timeTest(sort1, insertionSort, "InsertionSort")
    timeTest(sort2, selectionSort, "SelectionSort")
    timeTest(sort3, bubbleSort, "BubbleSort")
    # timeTest(sort4, mergeSort, "MergeSort")

main()
#os.system("pause")
