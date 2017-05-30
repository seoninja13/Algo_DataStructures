# build a class Link list from scratch eample 2:
class Node(object):
    def __init__(self,myData):
        self.data=myData
        self.next=None

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next=nextNode

    def getData(self):
        return self.data

    def setData(self,myData):
        self.data= myData 

class LinkedList(object):
    def __init__(self, myHead=None):
        self.head=myHead
        self.listSize=0
    
    def isEmpty(self):
        return self.head==None
                   
    def add(self,item):
        newNode=Node(item)
        newNode.setNext(self.head)
        self.head=newNode

    # implement size, search, and remove using 'linked list traversal'
    def size(self):
        size=0
        curr=self.head
        while curr != None:
            curr=curr.getNext()
            size +=1

        return size 

    def search(self, item):
        found=False
        curr=self.head
        while curr !=None and not found:
            if curr.getData()==item:
                found=True
            else:                   
                curr=curr.getNext()

        return found  

    def remove(self, item):
        curr=self.head
        prev=None 
        found=False
        
        while not found:
            if curr.getData() == item:
                found=True
            else:    
                prev=curr
                curr=curr.getNext()

        if  prev==None:
            self.head=curr.getNext()
        else:
            prev.setNext(curr.getNext())

        return found    
                
# ============================================
   
myLL=LinkedList()
myLL.add(1)
myLL.add(3)
myLL.add(5)
myLL.add(7)
myLL.add(9)
print("List size before removal is: "+ str(myLL.size()))
print("5 Is found before removal: " + str(myLL.search(55)))
print("Item is found: " + str(myLL.remove(55)))
print("List size after removal is: " + str(myLL.size()))
print("5 Is found after removal: " + str(myLL.search(55)))


# def remove(self,item):
                    

        
                        

    
            
        



