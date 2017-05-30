# # find the sum of the first n integers
# import time

# def sumOfN1(n):
#     start = time.time();
#     sum=0;    
#     for i in range(1,n):
#         sum+=i
#     end=time.time();

#     return end-start;    
# print("----------- START sumOfN1 ------------");
# print(sumOfN1(10000));
# print(sumOfN1(100000)); 
# print(sumOfN1(1000000));
# print("--------- END sumOfN1 ---------");


# def sumOfN2(n):
#     start = time.time();
#     print((n*(n+1)/2));
#     end = time.time();
#     return end-start;
    
# print(sumOfN2(10000));
# print(sumOfN2(100000)); 
# print(sumOfN2(1000000));

# def repeat(rep):
#     start = time.time();
#     for i in range(1,rep):
#         sumOfN2(10000);
#     end=time.time();
#     return end-start;        

# print(repeat(1000));        

def compr(myList):
    res = [x*x for x in myList]
    print(res)

compr([2,3,4]);
    
print("------------------------------------")

def compr2(n):
    res2 = [x*2 for x in range(n)]
    print(res2)

compr2(10);   
