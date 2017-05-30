# # # ==> Find the greatest common divisor of two numbers
# # def gcd(a,b):
# #     if a>b:
# #         for i in range(2,b):
# #             if b % i & a % i ==0:
# #                 print(b/i)
# #                 #return b/i;

# # gcd(25,10);                
        
    
# ===> GCD , Interactive python solution
# def gcd(m,n):
#     while m%n != 0:
#         oldm = m
#         oldn = n
        
#         m = oldn
#         n = oldm%oldn
#     return n

# print(gcd(30,9))            

# def compr(myList):
#     res = [x*x for x in range(0,len(myList-1))]
#     print(res)

# print("List compr is " + str(compr([2,3,4])))

# ===> Find the greatest common divisor ( My own solution)
# def gcd(a,b):
#     while a%b !=0:
#         newa=b
#         newb=a%b 

#         a=newa
#         b=newb       
                     
#     return b        

# print(gcd(8,24))            
                

