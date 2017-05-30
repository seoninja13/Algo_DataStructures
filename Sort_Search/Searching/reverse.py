from collections import deque
# # ==> Reerse a string
# # Input_file”  content: “Python is awesome!” 
# # Output_file” output: “!emosewa si nohtyP”

# ===> Example 1: Using 'Range'
# def reverse1(aString):
#     strLen=len(aString)
#     newStr=""
    
#     for i in range(strLen):
#         newStr+=aString[strLen-i-1]

#     return newStr

# print(reverse1("Python is awesome!"))    

# ===> Example 2: Using recursive function
# def rev(aString):
#     if len(aString)<=1:
#         return aString 

#     return rev(aString[1:])+ aString[0]
# print(rev("abc de"))        
                
# ===> Example 3: Append to an empty List
# def rev(aString):
#     counter=1
#     newStr = []
#     strLen= len(aString)

#     for i in range(0,strLen):
#         newStr.append(aString[strLen-counter]) 
#         counter +=1

#     newStr = "".join(newStr)
#     return newStr    

# print(rev("abc de"))

# ===> Example 4: Using 'Dequeue'
# def reverse1(aString):
#     d=deque()
#     d.extendleft(aString)
#     return "".join(d)
            
# print(reverse1("Python is awesome!")) 

# ========== REPEAT ================ 
# recursive reverse function
# def rev1(aString):
#     if len(aString)==0:
#         return aString
#     else:
#         return rev1(aString[1:])+ aString[0]  

# print(rev1("abcd"))
# ===============================================

     



   
