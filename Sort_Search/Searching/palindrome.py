#from collections import deque

# check if the string is palindrom, it should read same from left and right.
# ===> Solution 1: Using deque
# def isPalindrome1(aString): 
#     myDeque = deque()
#     for char in aString:
#         myDeque.append(char)

#     pos =0
#     isMatch = True    
#     while pos<len(myDeque) and isMatch:
#         if myDeque.popleft()==myDeque.pop():
#             pos+=1
#         else:
#             isMatch=False 

#     return isMatch

# print(isPalindrome1("aradara"))    

# ===> Solution 1.2: Using deque
# def isPalindrome1_2(aString): 
#     myDeque = deque()
#     for char in aString:
#         myDeque.append(char)

#     pos =0
#     isMatch = True    
#     while pos<len(myDeque) and isMatch:
#         if myDeque.popleft()==myDeque.pop():
#             pos+=1
#         else:
#             isMatch=False 

#     return isMatch

# print(isPalindrome1_2("aradara"))    

# # ===> Solution 2: using for loop with creating new 'list'.
# def isPalindrome2(aString):
#     myList=list(aString)
#     lenList=len(myList)
     
#     isMatch = False
#     i =0   
#     for pos in range(lenList):# comparing myList[i] AND myList[listLen-i];
#         if myList[i]== myList[lenList-i-1]:
#             isMatch=True
#         else:
#             return isMatch    
        
#     return isMatch

# print(isPalindrome2("ksradarsk"))    
        

 # ===> Solution 3: using while with creating new 'list'
# def isPalindrome3(aString):
#     myList=list(aString)
#     lenList=len(myList)
    
#     isMatch = True
#     pos =0
#     while pos<lenList and isMatch:
#         if myList[pos]==myList[lenList-pos-1]:
#             pos +=1
#         else:
#             isMatch=False   
                    
#     return isMatch

# print(isPalindrome3("radar"))   

# ===> Solution 4.1: Using recursion
# def isPalindrome4(aString):
#     return aString==aString[::-1]
    
# print(isPalindrome4("radar"))

# ===> Solution 5: Using 'while' and same 'sring'.
# def isPalindrome(aString):
#     pos=0
#     isMatch=True

#     while pos<len(aString) and isMatch:
#         if aString[pos]==aString[len(aString)-1-pos]:
#             pos+=1
#         else:
#             isMatch=False

#     return isMatch         

# print(isPalindrome("pradarpl")) 

# def isPalindrome(aString): # using recursion
#     return aString==aString[::-1]

# print(isPalindrome("robot"))   

# 0123456    // indexes
# 1234567   // length



Write a sum method which will work properly when invoked using either syntax below.

for (var i = 0; i < 5; i++) {
  var btn = document.createElement('button');
  btn.appendChild(document.createTextNode('Button ' + i));
  btn.addEventListener('click', function(){ console.log(i); });
  document.body.appendChild(btn);
}