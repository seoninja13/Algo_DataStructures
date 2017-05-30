import re
#  Write a function that interprets this input and outputs the number of hits that were recorded on each domain AND each domain under it. For example, a click on "sports.yahoo.com" counts for "sports.yahoo.com", "yahoo.com", and "com".

# Expected output (in any order):
# 1320    com
# 900    google.com
# 410    yahoo.com
# 60    mail.yahoo.com
# 10    mobile.sports.yahoo.com
# 50    sports.yahoo.com
# 10    stackoverflow.com
# 3    org
# 3    wikipedia.org
# 2    en.wikipedia.org
# 1    es.wikipedia.org

counts = [   "900,google.com",
             "60,mail.yahoo.com",
             "10,mobile.sports.yahoo.com",
             "40,sports.yahoo.com",
             "300,yahoo.com",
             "10,stackoverflow.com",
             "2,en.wikipedia.org",
             "1,es.wikipedia.org" ]

# ================ BEGIN SOLUTION ==================================

# Step 1: Sort out each List element with Regex for '.com','.org", etc.
# sorting '.com'
def sortByExt1(counts): 
    sortedExts1=[]
    for com in counts:
        dotCom=re.search(".com",com)
        if dotCom:
            sortedExts1.append(com)
    return  sortedExts1

sortByExt1(counts)

# sorting '.org'
def sortByExt2(counts):
    sortedExts2=[]
    for org in counts:
        dotOrg=re.search(".org",org)
        if dotOrg:
            sortedExts2.append(org)
    return  sortedExts2

sortByExt2(counts) 

# split each list, add the hits in a 'hitsSumCom', 'hitsSumOrg'.

list1,list2=sortByExt1(counts),sortByExt2(counts)
list1Sum, list2Sum=[],[] # new list wwith added the sum off all '.com' and '.org' hits.

# build the updated list1 with '.com' added to it at pos.0
def list1SumAll():
    for i in list1:
        list1Sum.append(i.split(","))
    # sum of all '.com' hits
    comSum=0
    for k in list1Sum:
        comSum += int(k[0])
    
    return comSum    
list1SumAll()

# insert the total sum at pos. 0 
list1Sum.insert(0,[list1SumAll(),".com"])
print(list1Sum)

# build the updated list2 with '.com' added to it at pos.0
# def list2SumAll():
#     for i in list2:
#         list2Sum.append(i.split(","))
#     # sum of all '.com' hits
#     orgSum=0
#     for k in list2Sum:
#         orgSum += int(k[0])
     
#     return orgSum    
# list2SumAll()
# # insert the total sum at pos. 0 
# list2Sum.insert(0,[list2SumAll, ".org"])

# adding the 2 lists together
#list1All,list2All=[],[]
# list1All=list1SumAll()
# print(list1All)
# list1All, list2All=list1SumAll(),list2SumAll()
# listAll=list1Sum + list2Sum
# print(listAll)
# for i in list1All:
#     print(i)

# for k in list2All:
#     print(k) 

# print("======== New list below ==========")
# for i in listAll:
#     print(i)
