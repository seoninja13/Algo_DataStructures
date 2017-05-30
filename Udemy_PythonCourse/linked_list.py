class Node(object): # .next=None
   def __init(self,data):
       self.myData=data
       self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0

    def insertStart(self,data): # O(1)
        self.size +=1
        newNode=Node(myData)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def size(self): #O(1)
        return self.size

    def size(self): # O(n)
        actualNode=self.head # actualNode=current
        size=0
        while actualNode is not None:
            size +=1
            actualNode = actualNode.nextNode
        return size 

    def insertEnd(self,myData): # O(n) because insertina t the end have to got rought the whole LL
        self.size +=1
        newNode=Node(myData)
        actualNode=self.head
        while actualNode.nextNode != None:
            actualNode=actualNode.nextNode

        actualNode.nextNode=newNode

    def traverseList(self):
        actualNode=self.head
        while actualNode is not None:
            actualNode=actualNode.nextNode

# using traversal implemnt 'size','search','remove' methods
    def size(self):
        curr=self.head
        size=0
        while curr != None:
            curr=
                    



        
            



            
            
                    
        

                
            




        
           

   
            

         
