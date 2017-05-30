# ===> Example 1: 
# ef extendList(val, list=[]):
#     list.append(val)
#     return list

# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')

# print ("list1 = %s" % list1) # list1 = 
# print ("list2 = %s" % list2)
# print ("list3 = %s" % list3)

# def extendList(val,list=None):
#     if list is None:
#         list=[]
#     list.append(val)
#     return list    

# ===> Example 2: What will be the output of the code below? explain why.
# def multipliers():
#     return [lambda x : i * x for i in range(4)] # range=0,1,2,3; return=0,2,4,9
    
# print [m(2) for m in multipliers()]
 
# ===> Ecxample 3: What will be the output of the code below?
# class Parent(object):
#     x = 1

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# print Parent.x, Child1.x, Child2.x
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x
# ===============================================================
# ===> Example 4: What will be the output below in P2? What about P3?
# from __future__ import division
# def div1(x,y):
#     print "%s/%s = %s" % (x, y, x/y)
    
# def div2(x,y):
#     print "%s//%s = %s" % (x, y, x//y)

# div1(5,2)   # 2
# div1(5.,2)  # 2
# div2(5,2)   # 2
# div2(5.,2.) # 2.0

# === Python3 ===
# def div1(x,y):
#     print("%s/%s = %s" % (x, y, x/y))
    
# def div2(x,y):
#     print("%s//%s = %s" % (x, y, x//y))

# div1(5,2)   # 2
# div1(5.,2)  # 2
# div2(5,2)   # 2
# div2(5.,2.) # 2.0

# ===> Example 5: Given a list of N numbers,produce List Comprehension...., read more

# [x for x in list[::2] if x%2=0]  # list[::2]--> even indexes

# ===> Example 6: given the following subclass of Dictionary
#class DefaultDict(dict):
# def __missing__(self, key):
#     return []
# #Will the code below work? Why or why not?

# d = DefaultDict()
# d['florp'] = 127

# A/ it will work, because with the Implementation of the DefaultDict class, whenever a key ismissing, the instance of the dictionary will automatically be instantiated with a list.

# def multipliers():
#       return [lambda x,i=i : i * x for i in range(4)] 
    
# print [m(2) for m in multipliers()]

# # range 0,1,2,3 ; res !=0,2,4,6; res=[]

# ===============================================
# class Parent(object):
#     x = 1

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# print Parent.x, Child1.x, Child2.x # 1,1,1
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x # 1,2,1
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x # 3,2,3

# ==================================================
# // operator will always perform interger division, regardless of the operand types
# class Parent(object):
    #     x = 1

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# print Parent.x, Child1.x, Child2.x # 1,1,1
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x # 1,2,1
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x # 3,2,3

# [x for x in list[::2] if x%2==0] # list[::2] are even indices, x%2 are even value
# ============================================
# Given the following subclass of dictionary:

# class DefaultDict(dict):
#   def __missing__(self, key):
#     return []

# Will the code below work? Why or why not?

# d = DefaultDict()
# d['florp'] = 127
# ------------------------------

# def extendList(val, list=[]):
#     if list is None:
#         list=[]
        
#     list.append(val)
#     return list

# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')

# print "list1 = %s" % list1
# print "list2 = %s" % list2
# print "list3 = %s" % list3

# =============================
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b

    return a
print fib(5)

# 0,1,1,2,3,5