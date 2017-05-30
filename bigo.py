# a=5
# b=6
# c=10
# for i in range(n):
#    for j in range(n):
#       x = i * i 
#       y = j * j
#       z = i * j
# for k in range(n):
#    w = a*k + 45
#    v = b*b
# d = 33

def compr(myList):
    res = [x*x for x in range(0,len(myList-1))]
    print(res)

print("List compre is " + str(compr([2,3,4]))
