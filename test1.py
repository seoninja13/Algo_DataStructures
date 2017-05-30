import time
from timeit import Timer

print(" ------ START test1 ----- ") # concatenate
def test1(): 
    list1 = []
    for i in range(10):
        list1 += [i]   
test1();

print(" ------ START test2 ----- ") # append
def test2(): 
    list2 = []
    for i in range(10):
        list2.append(i)   
test2();

print(" ------ START test3 ----- ") # list comprehension
def test3():
    list3 = [i for i in range(10)]
test3()

print(" ------ START test4 ----- ") # list range
def test4():
    list4 = list(range(10))
test4()

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t1.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("list comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

