def append_to(element,to=[]): # a new list is created once the function is defined, and then the same list is used in each successive call
    to.append(element)
    return to 

def append_to(element,to=None):
    if to is None:
        to =[]
    to.append(element)
    return to

myList=append_to(13)
print(myList)

myList2=append_to(27)
print(myList2)
