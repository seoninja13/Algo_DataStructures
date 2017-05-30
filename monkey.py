import random

# ==> func #1:generating a random string of 26 characters
def genString(strLen):
    alphabet = "abscdefghijklmnopqrstuvwxyz "
    res = "";
    for i in range(strLen):
        res += alphabet[random.randrange(27)]
    return res;

# ==> func #2:score each string
#iterate trough each character in old and a new one, and compare.Divide by length and find the score match in %
def scoreString(goal, testString):
    numSame = 0  
    for i in range(len(goal)):
        if goal[i]== testString[i]:
            numSame +=1;
    return numSame/len(goal)

print(scoreString("methinks it is like a weasel", genString(28)))

# ==> func #3:repeatedly generate score until score hits percentage
def repeatAll():
    result = scoreString("methinks it is like a weasel", genString(28))

    for i in range(0,100):
        print(scoreString("methinks it is like a weasel", genString(28)))
        #result
        # if result[i] >= float(score):
        #     return ("Score is: " + result)

repeatAll()


# NOTE: It is not completely solved, almost. I dont have the "best" option where
    
