class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == [];

    def enqueue(self, item):
        return self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items) 

q = Queue();
print("Enqueue 1 is: " + str(q.enqueue(11)))
print("Enqueue 2 is: " + str(q.enqueue(13)))
print("Enqueue 3 is: " + str(q.enqueue("Dog")))
print("The size is: " + str(q.size()))         
           
        
