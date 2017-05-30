import re
def displaySort(counts):
    
    #1 Iterate and find  element containing '.com', '.org' in a separate object
    contCom,contOrg=[],[]
    for i in counts:
        isCom = re.search(r".com",i)
        print(type(isCom))
        print("isCom is: " + str(isCom))

        split1=isCom.split(",")
        print(split1[0] + " " + split1[1])
        
        print("i is: " + i)
        print(type(i))
        contCom.append(isCom)
    
    return contCom    
       
    #2 split the number
    #3 add them up in a new sum, create new object

    # print(30*"=")
    # mySplit=counts[0].split(",")
    # print(mySplit[0]+ " " + mySplit[1])
    
print(displaySort([   "900,google.com",
             "60,mail.yahoo.com",
             "10,mobile.sports.yahoo.com",
             "40,sports.yahoo.com",
             "300,yahoo.com",
             "10,stackoverflow.com",
             "2,en.wikipedia.org",
             "1,es.wikipedia.org" ]))
