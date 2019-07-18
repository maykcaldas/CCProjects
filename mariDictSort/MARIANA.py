def selectionSort(valueToSort, nameToSort):
    '''
        The selection sort algorithm search the list len(list) times.
        At each search, it changes the position of the smaller element of the list with the current position of the search. 
    '''
    for i in range(len(valueToSort)):
        minPos = i
        for j in range(i, len(valueToSort)):
            if valueToSort[j] < valueToSort[minPos]:
                minPos = j
        valueToSort[minPos], valueToSort[i] = valueToSort[i], valueToSort[minPos]
        nameToSort[minPos], nameToSort[i] = nameToSort[i], nameToSort[minPos]

    return nameToSort, valueToSort
    
    
def createDict(fileToRead):
    dict={}
    for line in fileToRead:
        dict[line.split()[0]]=float(line.split()[1])
        
    return dict

def sepDict(dict):
    name=[]
    value=[]
    for i in dict:
        name.append(i)
        value.append(dict[i])
        
    return name, value
    
def main():
    toSort = open("MARIANA.dat", "r")
    toWrite = open("sortedMARIANA.dat", "w")
    data = createDict(toSort)
    
    name, value = sepDict(data)
    
    sortedName, sortedValue = selectionSort(value, name)
    
    for k in range(len(sortedName)):
        toWrite.write("{0:10s} {1:10.5f}\n".format(sortedName[k], sortedValue[k]))
    

if __name__ == "__main__":
    main()
