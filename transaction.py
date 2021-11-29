from queue import Queue
import time

def setExclusiveLock(Locks, a, idx, sequence):
    if (a.getAction(idx) == 'W' or (a.getAction(idx) == 'R')):
        sequence.enqueue(('XL', a.getTransaction(idx), a.getVar(idx)))
        Locks.enqueue((a.getVar(idx), a.getTransaction(idx)))
        print('exclusive locks of', a.getVar(idx), "in transaction", a.getTransaction(idx))
        print('XL'+a.getTransaction(idx)+'('+a.getVar(idx)+')')

def setUnlock(Locks, a, idx, sequence):
    if (a.getAction(idx) == 'C'):
        var = []
        for elmt in Locks.items:
            if(elmt[1] ==  a.getTransaction(idx)):
                var.append(elmt[0])
        for variable in var:
            sequence.enqueue(('UL', a.getTransaction(idx), variable))
            lockidx = Locks.findIdx((variable, a.getTransaction(idx)))
            Locks.dequeueAtIdx(lockidx)
            print('UL'+a.getTransaction(idx)+'('+variable+')')

def isLock(Locks, a, idx):
    var = []
    trans = []
    for elmt in Locks.items:
        var.append(elmt[0])
    if (a.getVar(idx) in var):
        return True

def isAvailable(Locks, a, idx):
    if(a.getAction(idx) != 'C'):
        trans = []
        for elmt in Locks.items:
            if(elmt[0] == a.getVar(idx)):
                trans.append(elmt[1])
        if (isLock(Locks, a, idx) and a.getTransaction(idx) not in trans):
            return False
    return True
        
def isTransactionAvailable(Locks, a, idx):
    if (isAvailable(Locks, a, idx)):
        for i in range(idx):
            if(a.getTransaction(i) == a.getTransaction(idx)):
                return False
        return True
    return False

a = Queue()
text_file = open("a.txt", "r")
lines = text_file.read().split(',')
for elmt in lines:
    if(elmt[0] == 'C'):
        a.enqueue((elmt[0], elmt[1]))
    else: 
        a.enqueue((elmt[0], elmt[1], elmt[2]))
print("input file: ")
a.printQueue()



sequence = Queue()
Locks = Queue()
i = 0
while (a.size() > 0):
    if(isTransactionAvailable(Locks, a, i)):
        setExclusiveLock(Locks, a, i, sequence)
        setUnlock(Locks, a, i, sequence)
        sequence.enqueue(a.items[i])
        if(a.getAction(i) != 'C'):
            print(a.getAction(i)+a.getTransaction(i)+'('+a.getVar(i)+')')
        else: 
            print(a.getAction(i)+a.getTransaction(i))
        a.dequeueAtIdx(i)
    else:
        i += 1
    if (i == a.size()):
        i = 0
    # time.sleep(8)