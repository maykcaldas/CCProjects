# -*- coding: utf-8 -*-
 
import os
#import numpy as np

def sorting(listToSort):
    sort=[]
    for i in range(len(listToSort)):
        min = i
        j=i
        while (j<len(listToSort)):
            if listToSort[j] < listToSort[min]:
                min = j
            j+=1
        sort.append(listToSort[min])
        listToSort[i], listToSort[min] = listToSort[min], listToSort[i]

        
        # for i in range(len(listToSort)):
        #     if listToSort[j] < listToSort[min]:
        #         min = j
        # sort.append(listToSort[min])
        # listToSort[i], listToSort[min] = listToSort[min], listToSort[i]
        


    return sort


def main():
    inp = input("Insira uma tupla de números: ")
    
    stringInput=inp.split()
    listToSort=[]

    if all([k.isdigit() for k in stringInput]) is True:
        for d in stringInput:
            listToSort.append(float(d))
            

        print("{0:^20s}: {1}".format("A entrada foi", listToSort))
        print("{0:^20s}: {1}".format("Função sorted()", sorted(listToSort)))
        print("{0:^20s}: {1}".format("Subrotina sorting()", sorting(listToSort)))

    else:
        print("Inserir somente números separados por espaços")



main()
os.system("pause")