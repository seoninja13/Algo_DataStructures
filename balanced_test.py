from pythonds.basic.stack import Stack

""" If there is an open parenthesis, push it to the stack as a symbol that a closing parenthesis is needed.
If there is an closing parathesis, pop the "open" parenthesis from the stack. That way at the end the stack should be empty. If not, it will return "False"."""

def isPair(parString):
    
    s = Stack()
    balanced = True;
    index =0

    while index < len(parString) and balanced:
        #print(index)
        symbol = parString[index]
        #print(symbol)
        if symbol == "(":
            s.push(symbol)
        else:               
            if s.isEmpty():
                balanced = False # checking if the string is empty
            else:
                s.pop()

        index +=1

    if balanced and s.isEmpty():
        return True
    else:
        return False
     
print(isPair("((())")) 


