# import re

# def test():
#     #res=re.search(".com", "The is the best i found avc.com")
#     if re.search(".com", "The is the best i found avc.com"):
#         print("Contains .com")
#     else:
#         print("Does NOt contain .com")    

# test() 
# 
# Write a Stack class

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        return self.items.append(item)

    def isEmpty(self):
        return  self.items==[] 

    def pop(self):
        #self.items.remove[0]
        return self.items.pop()

    def peek(self):
        return self.items[(len(self.items)-1)]

    def size(self):
        return len(self.items)
                          
def peekInto():
    myStack=Stack()
    myStack.push("a")
    print(myStack)
    myStack.push("b")
    print(myStack)
    print(myStack.peek())

