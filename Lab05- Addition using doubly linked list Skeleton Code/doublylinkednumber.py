class ListNode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail
    
    def _addbetween(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def addfirst(self, item):
        self._addbetween(item, None, self._head)
        
    def addlast(self, item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def removefirst(self):
        return self._remove(self._head)

    def removelast(self):
        return self._remove(self._tail)
    
    def __len__(self):
        return self._length


## To-do : Complete the tolinkednumber and __str__ funtions.
class DoublyLinkedNumber(DoublyLinkedList):
    def tolinkednumber(self, string):
        string = str(int(string))
        for j in string:
            self.addlast(j)
                    
    def __str__(self):
        cur = self._head
        s = ''
        while cur:
            s += str(cur.data)
            cur = cur.link
        return s
        
def sumlinkednumbers(dll1, dll2):
    dllsum = DoublyLinkedNumber()
    cur1 = dll1._tail
    cur2 = dll2._tail
    carry = 0
    
    while cur2 or cur1:       
        if cur2 == None:
            data1 = cur1.data
            sumcur = int(data1) + carry
            cur1 = cur1.prev
        elif cur1 == None:
            data2 = cur2.data           
            sumcur = int(data2) + carry
            cur2 = cur2.prev
        else:
            data1 = cur1.data
            data2 = cur2.data
            sumcur = int(data1) + int(data2) + carry
            cur1 = cur1.prev
            cur2 = cur2.prev
            
        if sumcur >= 10:
            carry = 1
        else:
            carry = 0
        dllsum.addfirst(sumcur-carry*10)
    return dllsum


## Do not change the code below. For testing purposes.          
s1 = '15'
dll1 = DoublyLinkedNumber()
dll1.tolinkednumber(s1)

s2 = '5'
dll2 = DoublyLinkedNumber()
dll2.tolinkednumber(s2)

print(dll1, "+", dll2, "=", sumlinkednumbers(dll1, dll2))
