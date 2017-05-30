import time
from timeit import Timer

# popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
# popend = timeit.Timer("x.pop()", "from __main__ import x")

# # x = list(range(2000000))
# # popzero.timeit(number=1000)

# # x = list(range(2000000))
# # popzero.timeit(number=1000)

# popzero = Timer("x.pop(0)",
#                 "from __main__ import x")
# popend = Timer("x.pop()",
#                "from __main__ import x")
# print("pop(0)   pop()")
# for i in range(1000000,100000001,1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" %(pz,pt))

# for i in range(0,25,5):
#     print(i) 
#     x= list(range(i))
#     print(x)  
#     popEnd = x.pop()
#     print(popEnd)
#     print("------------------------")

def list1(l):
    for i, j in l.items():
        print(i)
        print(j)
        print("----------");
        # p = alist1.pop(0)
        # print(p)
list1({"1":"aaa","2":"bbb","3":"ccc"});        