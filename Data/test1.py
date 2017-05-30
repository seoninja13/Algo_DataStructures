#input1=[1,2,3,4,5,6,7]
#input2=[ [1,4], [1,5], [4,2], [4,3], [2,3] ]
input1=["a","b","c","d"]
input2=[ ["a",4], ["a",5], ["b",4], ["b",3], ["c",7] ]

# Output below:
#a: 4,5
#b: 4,3
#c: 7
#d: None

# ============= START CODE ===================
myDict={}
relationships = [];
# Solution 1:
for k in input2:
    newRelationship = {}
    newRelationship["friend_id"] = k[0]
    newRelationship["user_id"]= k[1]
    relationships.append(newRelationship);
# Solution 2:    
    if k[0] not in myDict:
        myDict[k[0]] = [];
    if k[1] not in myDict:
        myDict[k[1]] = [];    
    myDict[k[0]].append(k[1])
    myDict[k[1]].append(k[0])

print(myDict)
print(relationships)

for i,k in myDict.items():
    print("%s has the corresponding %s" % (i,k))

# =========== END CODE ================

# for i in input1:
#     print(i)
# for k in input2:
#     print(k[1])

# dict1={}
# dict1[1]=10
# dict1[2]=20
# dict1[3]=30
# print(dict1)

