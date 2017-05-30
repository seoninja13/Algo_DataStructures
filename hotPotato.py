from pythonds.basic.queue import Queue
""" Will use queue. Once a ful turnover is made, the first item will be equeued, and the cycle will continue again """

def hotPotato(myQueue, num): 
    q = Queue()
    qSize = len(q)
    count = 0

    while qSize >: 
        first = q.dequeue()
        count += 1
        q.enqueue(first)
        q.dequeue()
        qSize -= 1

    return qSize     

hotPotato(["a","b","c","d","e"],3)

