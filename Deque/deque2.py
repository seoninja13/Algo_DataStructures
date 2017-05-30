from collections import deque

def deq():
    d = deque('ghi')                 # make a new deque with three items
    for elem in d:                   # iterate over the deque's 
        print(elem.upper())

deq()        