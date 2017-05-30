# sum = lambda x,y:x+y
# print(sum(3,5))

# def multipliers():
#     return [lambda x : i * x for i in range(4)] # range=0,1,2,3; NOT return=0,2,4,9, but [3,3,3,3]
    
# print([m(2) for m in multipliers()]) # 2 * [3,3,3,3]= [6,6,6,6]
# =======================================
# def multipliers():
#   return [lambda x, i=i : i * x for i in range(4)]

# print([m(2) for m in multipliers()])
# ====================================================
# class Parent(object):
#     x = 1

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# print(Parent.x, Child1.x, Child2.x) # 1 1 1 
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x) # 1 2 1 
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x) # 3 2 3
# ==================================
def list1():
    list = [ [ ] ] * 5
    list[0].append(10)
    print(list)
# 2. list  # output? = [ [],[],[],[],[],[] ]
# 3. list[0].append(10) = [ [],[],[],[],[],[],50 ]
# 4. list  # output?
# 5. list[1].append(20)
# 6. list  # output?
# 7. list.append(30)
# 8. list  # output?

list1()

 

