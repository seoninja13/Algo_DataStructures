class Node(object):
    def __init__(self,init_data):
        self.data=init_data
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_Data):
        self.data=new_Data

    def setNext(self,new_next):
        self.next=new_next

class LinkedList(object):
    
    def __init__(self): # creating empty list by default
        self.head=None

    def isEmpty(self):
        if self.head==None:
            return True    
    #adding new item  with 'add' method
    def add(self,new_item):
        temp=Node(new_item)
        temp.setNext(self.head)
        self.head=temp
        
    def size(self):
        size=0
        curr=self.head
        # while curr is not None: 
        while curr != None:    
            curr=curr.getNext()
            size +=1
        return size 

    def search(self,an_item):
        # count=0
        lSize=newLL.size()
        curr=self.head
        found=False
        while curr is not None and not found:
            if curr.getData()==an_item:
                found=True
            else:
                curr=curr.getNext()    
                
        return found    

       
newLL=LinkedList()
newLL.add(1)
newLL.add(3)
newLL.add(5)
print("Size is: " + str(newLL.size()))
print(newLL.search(39))
# print(newLL.isEmpty()) 


    
    

         
