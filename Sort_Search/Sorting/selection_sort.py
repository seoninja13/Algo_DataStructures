# bubble sort. keep swaping the neighboring elements

def selectionSort(aList):
    for fillslot in range(len(aList)-1,0,-1):
        posOfMax=0
        for location in range(1,fillslot+1):
            if aList[location] > aList[posOfmax]:
                posOfmax == location
          
    return aList

print(bubbleSort([2,4,9,7,5]))    









