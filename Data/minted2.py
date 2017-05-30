# Suppose you are creating an internal networking site for your company. You have two data sets to work with. The first data set is the employees at your company, and the second is all the pairs of employees who are virtually friends so far. It does not matter which employee's ID is in which column, the friendships are bidirectional.
# 
# You want to know who’s friends with whom. You need to implement a function that, given the employees and friendships as parameters, returns this data in the form of an adjacency list representation. This is a mapping of each employee ID to a list of his/her friends on the site.
# 
employees_input = [
  "1,Richard,Engineering",
  "2,Erlich,HR",
  "3,Monica,Business",
  "4,Dinesh,Engineering",
  "6,Carla,Engineering",
]

friendships_input = [
  "1,2",
  "1,3",
  "2,4",
]

# 1: 2, 3
# 2: 1, 4
# 3: 1
# 4: 2
# 6: None

# ============ SOLUTION 1 ================
# myDict={}
# def employee(input1):
#     tempList=[]
#     indexList=[]
#     for i in input1:
#         tempList.append(i)
        
#     for k in tempList:
#         k.split(",")
#         #print(k[0])
#         indexList.append([k[0])
        
#     return indexList   
        
# employee(employees_input)       

# def friends(input2):
#     tempList2=[]
#     indexList2=[]
#     for i in input2:
#         tempList2.append(i)
        
#     for k in tempList2:
#         k.split(",")

#         if k[0]=1: # push as value into indexList2

# friends(friendships_input)
            
            
# def relations(param1,param2):
    
#     return 1
    
# ============ SOLUTION 2 =====================
def relations(input1,input2):
    myDict={} # Dict to push into result from part1 and part2   
# part1: employee
    tempList=[]
    indexList=[]
    for i in input1:
        tempList.append(i)
        
    for k in tempList:
        k.split(",") # [ [1,Richard,Engineering] , [], [] ]
        #print(k[0])
        indexList.append(k[0]) # [1,2,3,4,6]
        
# part 2: friendships       
    tempList2=[]
    indexList2=[]
    for i in input2:
        tempList2.append(i)
        
    for k in tempList2:
        indexList2.append(k.split(",")) # [ [1,2], [1,3], [2,4] ]
    #print(indexList2)    

    for j in indexList:
        for n in indexList2:
            if j==n[0]:
                myDict[j]=n[1]    
                   
    print(myDict)    

          
relations(employees_input,friendships_input)
    

      