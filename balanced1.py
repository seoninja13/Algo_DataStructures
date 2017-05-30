from pythonds.basic.stack import Stack

# def isMatch(is_open,is_close):  
#     opens = "[({"
#     closers = "])}"
#     print(opens.index(is_open))
#     return opens.index(is_open) == closers.index(is_close);
#     from pythonds.basic.stack import Stack

# def isPair(parString):   
#     s = Stack()
#     balanced = True;
#     index =0
    
#     while index < len(parString) and balanced:
#         symbol = parString[index]

#         if symbol in "[({":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False;
#             else:
#                 top = s.pop()
#                 print(top)
#                 if not isMatch(top,symbol):
#                     balanced = False

#         index+=1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
        
# print(isPair("((()))")) 

# ===> Balanced parenthesis
# def isBalanced(aString):
#     isOpen=[ "(","{","[" ]  # count each position
#     isClosed=[ ")","}","]" ]  # count each position and match with position in open
#     posOpen,posClosed=0,0
#     myStack=Stack() #     ] [{(
#     isMatch=True    

# #2 if string starts with closed, return false
#     if aString[0] in isClosed:
#         isMatch=False 

#     for i in aString:
#         if aString[i] in isOpen:
#             myStack.push(aString[i])

#     posOpen=isOpen.index(aString[i])
#     print(posOpen)
            
                  


# isBalanced("({[]})")    

# # ===> "simple isBalanced prenthesis" DEMO
# def parChecker(symbolString):
#     s=Stack() 
#     balanced=True
#     index=0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol=="(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced=False
#             else:
#                 s.pop()

#         index +=1

#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False                        

# print(parChecker("((()))")) # "(", "(", "("  ,")"=pop(),  

# ===> Simple balanced prenthesis
# def parCheck(symbolStr):
#     balanced=True
#     pos=0
#     s=Stack() # create instance of Stack() class

#     while pos<len(symbolStr) and balanced:
#         if symbolStr[pos]=="(":
#             s.push(symbolStr[pos])
#         else:
#             if s.isEmpty():
#                 balanced=False
#             else:
#                 s.pop()
#         pos +=1

#     if s.isEmpty() and balanced:
#         return True
#     else:
#         return False

# print(parCheck("((()))]"))                       
                
# ===> Balanced parenthesis General case
def parCheck(symbolStr):
    balanced=True
    pos=0
    s=Stack()
    while pos<len(symbolStr) and balanced:
        symbol=symbolStr[pos]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top = s.pop()
                if not isMatch(top, symbol):
                    balanced=False
        pos +=1

    if s.isEmpty() and balanced:
        return True
    else:
        return False
            
def isMatch(opens,closers):
    isOpen="([{"
    isClosed=")]}" 
    return isOpen.index(opens)==isClosed.index(closers)


print(parCheck("{((()))}"))         