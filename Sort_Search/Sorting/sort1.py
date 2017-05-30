# bubble sort. keep swaping the neighboring elements

def bubbleSort(aList):
    for passnum in range(len(aList)-1,0,-1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
          
    return aList

print(bubbleSort([2,4,9,7,5]))    

# for num in range(10,20):
#     for i in range(2, num):       
#         if num%i==0:
#             j=num/i
#             print(%d equals %d *%d" ")








