# Example 1: find the fibonacy nth number
# def findFib(n):
#     a,b=0,1
#     if n<=1:
#         return 0
#     else:
#         for i in range(n):
#             a,b= b,a+b

#     return a

# print(findFib(6))           

# 0, 1, 1, 2, 3, 5, 8, 13, 21    // findFib(n)
# 0  1  2  3  4  5  6  7   8    //  n  
# a  b
#    a  b
#       aib  b
#           a   b


# Example 2: Using recursive function
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1) + fib(n-2)) 

print(fib(6))           
    

