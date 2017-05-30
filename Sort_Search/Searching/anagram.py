# check to see if the string are anagram
#since strings in python are immutabele,the first step in the process will be to convert the second string to a list.

# ===> Example 1: Checking off. see that each character in str1 occurs in str2
# def anagramSolution1(s1,s2):
#     alist = list(s2)

#     pos1 = 0
#     stillOK = True

#     while pos1 < len(s1) and stillOK:
#         pos2 = 0
#         found = False
#         while pos2 < len(alist) and not found:
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1

#         if found:
#             alist[pos2] = None
#         else:
#             stillOK = False

#         pos1 = pos1 + 1

#     return stillOK

# print(anagramSolution1('abcdk','dcban'))

# ===> Example 2: "Sort and compare"
def isAnagram(str1,str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()

    isMatch = True # there is match at index level
    pos =0

    while pos<len(str1) and isMatch:
        if list1[pos] == list2[pos]:
            pos+=1
        else:
            isMatch=False

    return isMatch            

print(isAnagram("abc","bca"))                

            
    


    
    



# def a():
#     s1="abc"
#     list1=[s1];
#     print(list1)
# a()    
