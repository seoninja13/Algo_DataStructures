from pythonds.basic.stack import Stack
import turtle
# ===> find sum of list of numbers using for loop
# def mySum(aList):
#     sum=0
#     for i in aList:
#         sum += i

#     return sum

# print("Sum of 'for loop' is: " + str(mySum([1,3,5,7,9])))

# ===> Recursively find sum of list of numbers 
# def fibSum(aList):
#     if len(aList)==1:
#         return aList[0]
#     else:
#         return  aList[0] + fibSum(aList[1:])

# print(fibSum([1,3,5,7,9]))  # 24         
    
# print("Sum of 'for loop' is: " + str(mySum([1,3,5,7,9])))      
# def fib(n):
#     return (fib(n-1)+fib(n-2))

# print(fib(5)) 

# 0  1  1  2  3  5  8  13  //  n-th element  
# 1  2  3  4  5  6  7  8   //  = fib(n)

# ((((1+3)+5))+7)+9)
# sum=(1+(3+(5+(7+(9))))
# sum=(1+(3+(5+(16)))
# sum=(1+(3+(21)))
# sum=(1+(3+(5+(7+(9))))

# ==> Find product using 'while' loop
# def fact(n):
#     total,k=1,1
#     while k<=n:
#        total=total*k
#        k+=1
#        print(total)

#     return total  

# print(fact(4))  # 1,2,3,4 

# ==> Find product using Factorial loop
# def factMult(n):
#     if n==1:
#         return 1
#     else:
#         return n*factMult(n-1) 

# print(factMult(4))
# 
# ===> Convert any integer to str with a base of 2-16
# convertString = "0123456789ABCDEF"  
# def toStr(myNum, base):
#     convertStr = "0123456789ABCDEF" # from base 2 to base 16
#     if myNum<base:
#         return convertStr[myNum]
#     else:
#         return toStr(myNum // 10, base) + convertStr[myNum % base] 
        
#     # rem =1453 % 10 = 3
#     # newNum = myNum // 10 = 145
#     # rem =newNum % 10 = 5
#     # newNum= newNum //10 = 14

# print(toStr(145,2))            

# ==> Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
# def revString(aString):
#     if len(aString)==1:
#         return aString[0]
#     else:
#         return revString(aString[1:]) + aString[0]

# print(revString("abcd"))

# ==> Write a palindrome in Recursive; 'radar', 'live not on evil'
# def isPalindrome(aString): !!! NOT WORKING !!!
#     isPalin=True
#     if aString[0] == aString[-1]:
#         return isPalindrome(aString[1:-1])
#     else:
#         isPalin=False

#     return isPalin

# print(isPalindrome("12321")) 

# def isPalindrome(aString):
#     if len(aString)<2:
#         return True
#     if aString[0] != aString[-1]:
#         return False
#     else:    
#         return isPalindrome(aString[1:-1])
  
# print(isPalindrome("9123219"))       

# ==> implementing Recursion with Stack Frames
# def toString(num, base):
#     convertString="0123456789ABCDEF"
#     rStack=Stack()
#     while num > 0:
#         if num<base:
#             rStack.push(convertString[num])
#         else:
#             rStack.push(num % base)
#         num=num // base
#     res=""        
#     while not rStack.isEmpty():
#         res=res + str(rStack.pop()) 

#     return res 

# print(toString(14545,10))


# ===> Turtle Drawings. draw a spiral recursively

# myTurtle=turtle.Turtle()
# myWin=turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen>0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

# # ===> Fractal drawing.
# def tree(branchLen,turn):
#     if branchLen>5:
#         turn.forward(branchLen)
#         turn.right(20)
#         tree(branchLen-15,t)
#         turn.left(40)
#         tree(branchLen-10,turn)
#         turn.right(20)
#         turn.backward(branchLen)

# def main():
#     turn=turtle.Turtle()
#     myWin=Turtle.Screensize()
#     turn.left(90)
#     turn.up()
#     turn.backwards(100)
#     turn.down()
#     turn.color("green")
#     tree(75,turn)
#     myWin.exitonClick()

# main()    
            

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()


# def toString(num, base):
#     rStack=Stack()
#     convertString="0123456789ABCDEF"
#     while num>0:
#         if num <base:
#             rStack.push(convertString[num])
#         else:
#             rStack.push(convertString[num % base])
#         num=num//base
#     res=""
#     while not rStack.isEmpty():
#         res=res + str(rStack.pop())
#     return res

# print(toStr(1453,16))           

# ===> Sierpinski  Triangle.
# import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle=turtle.Turtle()
    myWin=turtle.Screen() 
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    myWin.exitonclick() 

drawTriangle()



# def getMid(p1,p2):
#     return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# def sierpinski(points,degree,myTurtle):
#     colormap = ['blue','red','green','white','yellow',
#                 'violet','orange']
#     drawTriangle(points,colormap[degree],myTurtle)
#     if degree > 0:
#         sierpinski([points[0],
#                         getMid(points[0], points[1]),
#                         getMid(points[0], points[2])],
#                    degree-1, myTurtle)
#         sierpinski([points[1],
#                         getMid(points[0], points[1]),
#                         getMid(points[1], points[2])],
#                    degree-1, myTurtle)
#         sierpinski([points[2],
#                         getMid(points[2], points[1]),
#                         getMid(points[0], points[2])],
#                    degree-1, myTurtle)

# def main():
#    myTurtle = turtle.Turtle()
#    myWin = turtle.Screen()
#    myPoints = [[-100,-50],[0,100],[100,-50]]
#    sierpinski(myPoints,3,myTurtle)
#    myWin.exitonclick()

# main()
            
#   Changes made           
           

                


