def anagramSolution2(s1,s2):
    list1 = list(s1) # convert the string to a list
    list2 = list(s2)
    list1.sort() # sort the list
    list2.sort()

    pos = 0 # psotion in the list
    isMatch = True

    while pos < len(s2) and isMatch:
        if list1[pos] == list2[pos]:
            pos+=1
        else:
            isMatch = False;

    return isMatch

print(anagramSolution2("abcd","zcba"))