from pythonds.basic.stack import Stack

# """ Divide by 2 and push the remainder in a stack ( 0 or 1) """
# def decToBinary(decNumber):
#     s = Stack()   
#     while decNumber > 0:
#         rem = decNumber % 2   
#         s.push(rem)
#         decNumber = (decNumber - rem) // 2

#     binString = ""
#     while not s.isEmpty:
#         binString += str(s.pop()) 

#     return binString           
       
# print(decToBinary(67))  

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 16
        print(rem)
        remstack.push(rem)
        decNumber = (decNumber-rem) // 16

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString

print(divideBy2(256))





