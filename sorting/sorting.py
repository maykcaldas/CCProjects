# -*- coding: utf-8 -*-
 
import os
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
    '''The selection sort algorithm search the list len(list) times.
       At each search, it changes the position of the smaller element of the list with the current position of the search. 
       It has a O(n^2) complexity. '''
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

    sort = [5,67,1,1,0,-8,2,4,6,8,9,67,5,544,3,3,6,4,4,6]

    print(sort)
    print(insertionSort(sort))


    #inp = input("Insira uma tupla de números: ")
    #
    #stringInput=inp.split()
    #listToSort=[]

    #if all([k.isdigit() for k in stringInput]) is True:
    #    for d in stringInput:
    #        listToSort.append(float(d))
    #        

    #    print("{0:^20s}: {1}".format("A entrada foi", listToSort))
    #    print("{0:^20s}: {1}".format("Função sorted()", sorted(listToSort)))
    #    print("{0:^20s}: {1}".format("Subrotina sorting()", sorting(listToSort)))

    #else:
    #    print("Inserir somente números separados por espaços")



main()
#os.system("pause")
