# import re
# #  Write a function that interprets this input and outputs the number of hits that were recorded on each domain AND each domain under it. For example, a click on "sports.yahoo.com" counts for "sports.yahoo.com", "yahoo.com", and "com".

# # Expected output (in any order):
# # 1320    com
# # 900    google.com
# # 410    yahoo.com
# # 60    mail.yahoo.com
# # 10    mobile.sports.yahoo.com
# # 50    sports.yahoo.com
# # 10    stackoverflow.com
# # 3    org
# # 3    wikipedia.org
# # 2    en.wikipedia.org
# # 1    es.wikipedia.org


# counts = [   "900,google.com",
#              "60,mail.yahoo.com",
#              "10,mobile.sports.yahoo.com",
#              "40,sports.yahoo.com",
#              "300,yahoo.com",
#              "10,stackoverflow.com",
#              "2,en.wikipedia.org",
#              "1,es.wikipedia.org" ]

# # ====================================

# # Step 1: Sort out each List element with Regex for '.com','.org", etc.
# # def sortByExt(counts):
# #     sortedExts=[]
# #     comCount=0
# #     orgCount=0
# #     for com in counts:
# #         dotCom=re.search(".com",com)
# #         sortedExts.append(dotCom)
# #         print(sortedExts[comCount])
# #         comCount +=1

# #     return  sortedExts

# # sortByExt([   "900,google.com",
# #              "60,mail.yahoo.com",
# #              "10,mobile.sports.yahoo.com",
# #              "40,sports.yahoo.com",
# #              "300,yahoo.com",
# #              "10,stackoverflow.com",
# #              "2,en.wikipedia.org",
# #              "1,es.wikipedia.org" ])     
# newList=[]
# count=0
# for i in counts:
#     print(i)
#     newList.append(i)
#     print(newList[count])
#     count +=1
#     print("------ New Iteration -----------")

list1=[1,2,3]
list2=[4,5,6]
  
def test1():
    sum1=0    
    for i in list1:
        sum1+=i

    return sum1
test1()    

list1.insert(0,[test1(),"aaa"])
print("List1 is: + " + str(list1))    

def test2():
    sum2=0    
    for i in list2:
        sum2+=i

    return sum2
test2()    

list2.insert(0,test2())
print("List 2 is: " + str(list2)) 

listAll=list1+list2
print("List all is: " + str(listAll)) 


# list2=[4,5,6]
# list2.insert(0,"b")   

# print(" ===== LIST1 + LIST2 ===== ")
# newList=list1+list2
# print(newList)     