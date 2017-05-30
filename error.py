import math
anumber=int(input("Please, enter an integer: "))

if 0< anumber < 9:
    raise RuntimeError("Enter number >9")
elif anumber <0:
    raise RuntimeError("Enter a positve number ");
else:
    print(math.sqrt(anumber));   
