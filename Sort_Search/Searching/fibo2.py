# # === find the sum of Nth Fibonacinumbers ===
# # Example 1:
def fib(n):
    # a=0
    # b=1
    # c= a+b
    sum=0
    if n <=1:
        return n
    else:
        nthVal = (fib(n-1)+ fib(n-2))
        #print("The nthVal is: " + str(nthVal))
        for i in range(nthVal-1):
            #a,b,c=b,a+b,b+c
            print(i)
            sum = i
            sum += i
             
    return  ?????????      
                       
print(fib(6)) 

# #  0 1 2 3 4 5 6 7  8    //  n
# # [0,1,1,2,3,5,8,13,21] // fib(n) 
# #      a b c                     // Sum is 
# #        a b c     

# def test(n):
#     sum =0   
#     for i in range(5):
#         print(i)
#         sum =i
#         sum += i

#     return sum    
# print(test(5))        