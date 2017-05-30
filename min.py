import time
from random import randrange

# find minimum number in a list . O(n^2);
def minNum(myList):
    min = myList[0]

    for i in range(0,len(myList)):
        #min= myList[0];
        if myList[i] < min:
            min = myList[i]

    return(min);

#print(minNum([9,2,6,9,3,8]))          

def minNum2(myList2):
    min = myList2[0]

    for i in myList2:
        isMin = True
        for k in myList2:
            if i>k:
                isMin = False
        if isMin:
            min = i;

    return(min);
            
#print(minNum2([9,2,6,9,3,8])) 
print("----------------------")
# ==> Using List Comprehension
for listSize in range(1000,10001,1000):
    alist=[randrange(10000) for x in range(listSize)]
    start=time.time();
    print("Minimum is " + str(minNum(alist)));
    end = time.time();
    print("size: %d, time: %f" %(listSize, end - start))

# alist=[randrange(1005) for x in range(10)]
# print(alist)
# print(alist)
# print(alist)

