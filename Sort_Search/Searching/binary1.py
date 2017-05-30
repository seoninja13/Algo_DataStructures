def binarySearch(aList, item):
    start = 0
    end = len(aList)-1
    found = False

    while start<=end and not found:
        midpoint=(start + end)//2
        print(midpoint)
        if aList[midpoint] == item:
            found = True
        else:
            if aList[midpoint] < item:
                start = midpoint +1
            else:
                end = midpoint-1

    return found
		
print(binarySearch([1,3,7,9,13,17,20,23,28],230))
