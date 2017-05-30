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

    def append(self,item): # add element at the last position. Shifting all Node to the left
        curr=self.head
        found=False
        newNode=Node(item)
        # isSize=0
        while curr != None and not found:
            if curr.getNext() == None:
                curr.setNext(newNode)
                newNode.setNext(None)
                # isSize += 1
                found=True
            else:
                curr=curr.getNext() 

        return found  

    def insert(self, pos, item):
        # check if the list is empty
        # if it is then just call the add
        # method
        newItem = Node(item)
        done = False
        if self.size() == 0:
            self.add(newItem)
        else:
            current = self.head
            curpos = 0
            while current != None and not done:
                if pos == 1:
                    self.add(item)
                    done = True
                curpos += 1
                if curpos == pos - 1:
                    n = current.getNext()
                    newItem.setNext(n)
                    current.setNext(newItem)
                    self.lsSize += 1
                    done = True
                else:
                    current = current.getNext()

        return done

    # def insert(self, pos, item): 
    #     curr=self.head
    #     curr_next=curr.getNext()
    #     count=1
    #     done=False
    #     newNode=Node(item)
    #     while curr !=None and not found:
    #         if count -1 =pos:
    #             prev.setNext(get_data(newNode))
    #             newNode.setNext(curr_next)
    #             done=True
    #         else:
    #             curr=curr_next   
               
# ============================================
   
myLL=LinkedList()
myLL.add(1)
# myLL.add(3)
# myLL.add(5)
# myLL.add(7)
# myLL.add(9)
print("List size before append is is: "+ str(myLL.size()))
print("11 Is found before append: " + str(myLL.search(11)))
print("Item appended is: " + str(myLL.append(11)))
print("List size after append is: " + str(myLL.size()))
print("11 Is found after append: " + str(myLL.search(11)))
print(myLL)


                    

        
                        

    
            
        



