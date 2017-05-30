import timeit
from timeit import Timer
import random

# for i in range(10000,1000001,20000):
#     t= timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")

#     x=list(range(i))
#     list_time=t.timeit(number=1000)
#     x = {j:None for j in range(i)}
#     dict_time = t.timeit(number=1000)
#     print("%d,%10.3f,%10.3f" % (i,list_time,dict_time))

# def dict():
#     dict1 = {"a":"ana","b":"bob","c":"canoe"}
#     for k,v in dict1.items():
#         print(['k'])
#         #print(v)
#     #print("-----------------")

# dict() 

# def dict2():
#     dict2 = {"b":"bob","c":"canoe","a":"ana"}
#     for v in dict2:
#         vals = dict2[v]
#         if "bob" not in 
#         print([vals])
#         #print(v)
#     #print("-----------------")
# dict2()

# dict comprehension

def dict2():
    d2 ={x:x**2 for x in (3,5,7)}
    print(d2)
dict2()



