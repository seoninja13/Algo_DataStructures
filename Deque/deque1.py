#from pythonds.basic.deque import Deque
#from collections import deque


# Deque() - creates a new deque that is empty
# addFront()
# addRear()
# removeFront()
# removeRear()

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        return self.items.append()    

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self, item):
        return self.items.pop(0) 

    def size(self):
        return len(self.items) 

def deques():   
    d = Deque()
    d.addRear(1)
    d.addRear(2)
    print(d.removeRear(0))
    print(d.removeFront())
    print(d.isEmpty())

deques()    

 # fornt -> O(1)
 # Rear -> O(n)             
