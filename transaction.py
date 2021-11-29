from queue import Queue

def setExclusiveLock(Locks, soal, idx, solusi):
    if (soal.getAction(idx) == 'W' or (soal.getAction(idx) == 'R')):
        solusi.enqueue(('XL', soal.getTransaction(idx), soal.getVar(idx)))
        Locks.enqueue((soal.getVar(idx), soal.getTransaction(idx)))
        print('XL'+soal.getTransaction(idx)+'('+soal.getVar(idx)+')'+"; ", end="")

def setUnlock(Locks, soal, idx, solusi):
    if (soal.getAction(idx) == 'C'):
        var = []
        for elmt in Locks.items:
            if(elmt[1] ==  soal.getTransaction(idx)):
                var.append(elmt[0])
        for variable in var:
            solusi.enqueue(('UL', soal.getTransaction(idx), variable))
            lockidx = Locks.findIdx((variable, soal.getTransaction(idx)))
            Locks.dequeueAtIdx(lockidx)
            print('UL'+soal.getTransaction(idx)+'('+variable+')'+"; ", end="")

def isLock(Locks, soal, idx):
    var = []
    for elmt in Locks.items:
        var.append(elmt[0])
    if (soal.getVar(idx) in var):
        return True

def isAvailable(Locks, soal, idx):
    if(soal.getAction(idx) != 'C'):
        trans = []
        for elmt in Locks.items:
            if(elmt[0] == soal.getVar(idx)):
                trans.append(elmt[1])
        if (isLock(Locks, soal, idx) and soal.getTransaction(idx) not in trans):
            return False
    return True
        
def isTransactionAvailable(Locks, soal, idx):
    if (isAvailable(Locks, soal, idx)):
        for i in range(idx):
            if(soal.getTransaction(i) == soal.getTransaction(idx)):
                return False
        return True
    return False

soal = Queue()
text_file = open("input.txt", "r")
lines = text_file.read().split(',')
for elmt in lines:
    if(elmt[0] == 'C'):
        soal.enqueue((elmt[0], elmt[1]))
    else: 
        soal.enqueue((elmt[0], elmt[1], elmt[2]))

print("Soal: ", end="")
soal.printQueue()

print("Solusi: ", end="")

solusi = Queue()
Locks = Queue()
i = 0
while (soal.size() > 0):
    if(isTransactionAvailable(Locks, soal, i)):
        setExclusiveLock(Locks, soal, i, solusi)
        setUnlock(Locks, soal, i, solusi)
        solusi.enqueue(soal.items[i])
        if(soal.getAction(i) != 'C'):
            print(soal.getAction(i)+soal.getTransaction(i)+'('+soal.getVar(i)+')'+"; ", end="")
        else: 
            print(soal.getAction(i)+soal.getTransaction(i)+ "; ", end="")
        soal.dequeueAtIdx(i)
    else:
        i += 1
    if (i == soal.size()):
        i = 0