import collections
#kode ini dibuat bersama oleh harith fakhiri - 13519161 dari k1 dan haikal lazuardi- 13519027dari k3.

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(self.size(),item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def findIdx(self, elmt):
        return self.items.index(elmt)

    def dequeueAtIdx(self, idx):
        del self.items[idx]
        return self.items
        
    def printQueue(self):
        for i in range (self.size()):
            if (self.getAction(i) != 'C'):
                print(self.getAction(i)+self.getTransaction(i)+'('+self.getVar(i)+')', end='')
            else:
                print(self.getAction(i)+self.getTransaction(i), end='')
            if(i!=self.size()-1) :
                print("; ", end='')
            else:
                print()
                print()

    def getAction(self, idx):
        return self.items[idx][0]

    def getTransaction(self, idx):
        return self.items[idx][1]
    
    def getVar(self, idx):
        return self.items[idx][2]
