#sequentials earch
# def seqSearch(aList,item):
#     pos = 0
#     found = False
#     # for i in aList:
#     #     print(i)
#     #     if i == item:
#     #         break
#     #         return True;

#     while pos < len(aList) and not found:
#         if aList[pos] == item:
#             found = True
#         else:
#             pos +=1

#     return found            
            
# print(seqSearch([3,5,7,9,11,13],55)) 
# 
def search1(aList,aNum):
    found=False
    pos =0

    while pos<len(aList) and not found:
        if aList[pos] == aNum:
            found = True
        else:
            pos+=1

    return found

print(search1([2,33,45,23,17,66],45))