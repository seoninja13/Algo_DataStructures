# def stockPriceYesterday(myList):
    
def findMin(myList):
    min=myList[0]
    max=myList[0]
    lenList=len(myList)
    minPos,maxPos=0,0
    diff=max-min
  
    for i in range(0,lenList):
        if myList[i]< min:
            min=myList[i]
            minPos +=1
        if myList[i] > max:
            max= myList[i]
            maxPos+=1        
            
        print("The memebr is: " + str(myList[i]))

    print("Min is: " + str(min))
    print("Max is: " + str(max))
    print("minPos is: " + str(minPos))
    print("maxPos is: " + str(maxPos))
    return ("The difference is: " + str(diff))

print(findMin([100,10,5,30,20,50,95]))    
    
# prices=[50,100,150,75,60] ; have to find the minimum and maxim and subtract
# index 0 == earliest time
# for i in range(5):
#     print(i) #0,1,2,3,4,