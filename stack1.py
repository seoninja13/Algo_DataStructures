from pythonds.basic.stack import Stack

class Stack:
    def __init__(self):
        self.items=[];

    def isEmpty(self):
        return self.items ==[]

    def push(self,item):
        #self.items.append(item)
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
   
    # s=Stack();
    # print(s.push("Hello"));
    # print(s.push("Hello2"));
    # print(s.peek());
    # print(s.pop())
    # print(s.peek()) 

    # print(s.isEmpty())                   
    # #print(s.pop());
    # print(s.peek());

    m = Stack()
    m.push('x')
    m.push('y')
    m.push('z')
    while not m.isEmpty():
        m.pop()

    m.push("abz")
    print(m.peek())    

