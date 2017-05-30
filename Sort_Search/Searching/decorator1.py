# def func1(x):
#     return x+1

# print(func1(5))   

# func2= func1
# print(func2(5))

# # function decorators
# # class decorators

# def f():
    
#     def g():
#         print("Hi, it's me 'g'")
#         print("Thanks for calling me")
        
#     print("This is the function 'f'")
#     print("I am calling 'g' now:")
#     g()
  
# f()

# # result is below
# # Hi  it s me gaierror
# # Thanks for calling me
# # This is the function g
# # I am calling G now.

# x=5
# def printHam():
#     pass
# class Test:
#     pass 
# print dir()  
# 
# def outside(x=5):
#     x=55
#     def printHam():
#         print x
#     return printHam

# myFunc = outside(555)
# myFunc()    

# def addOne(myFunc):
#     def addOneInside():
#         return myFunc()+1
#     return addOneInside

# def oldFunc():
#     return 3

# newFunc = addOne(oldFunc) # decorating the "oldFunc" to add to the "addOne" function
# print oldFunc(),newFunc()
# ===== result below ====

# def f(x):
#     def g(y):
#         return y + x + 3 
#         #return 1   1   3 =5
#     return g

# nf1 = f(1)
# nf2 = f(3)

# print(nf1(1))
# print(nf1(1))
#===================================================
# Polynimial factory ax^2+bx + c
def pol_creator(a,b,c):
    def polynomial(x):
        return a*x*x + b*x +c
    return polynomial

p1=pol_creator(2,3,-1)
p2=pol_creator(-1,2,1)        

for x in range(-2,2,1):
    print(x,p1