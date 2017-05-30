# === Find nth Fibonaci element ===
# ==> Example 1: Using looping technique
def fib1(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
print(fib1(6))

# ==> Example 2: Using recursion
# def fib2(n):
#     if n<=1:
#         return n
#     else: 
#         return(fib2(n-1) + fib2(n-2))

# print(fib2(6))

# # ==> Example 3: Using recursion
# def fib2(n):
#     if n<=1:
#         return n
#     else: 
#         return(fib2(n-1) + fib2(n-2))

# print(fib2(6))         
     

# 0 1 2 3 4 5 6  7   (positions)
# 1 2 3 4 5 6 7  8    position)
# 0,1,2,3,5,8,13,21
 
# binary search
def binSearch(aList,item):
    first=0
    last=len(aList)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        id aList[midpoint]== item:
        found = True
        else:
            if item<aList[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1

    return found                     