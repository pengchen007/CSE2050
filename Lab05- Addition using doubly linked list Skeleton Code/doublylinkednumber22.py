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
        a = int(string)
        b = str(a)
        for i in b:
            self.addlast(int(i))

                    
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

    while cur1 is not None and cur2 is not None:
        if cur1.data + cur2.data >= 10:
            newd = cur1.data+cur2.data-10 + carry
            carry = 1
            dllsum.addfirst(newd)
        else:
            newd = cur1.data +cur2.data +carry
            carry = 0
            dllsum.addfirst(newd)
        cur1 =cur1.prev
        cur2 = cur2.prev
    if cur1 is None:
        while cur2 is not None:
            dllsum.addfirst(cur2.data+carry)
            carry = 0
            cur2 = cur2.prev
    else:
        while cur1 is not None:
            dllsum.addfirst(cur1.data + carry)
            carry = 0
            cur1 = cur1.prev
    return dllsum
    



## Do not change the code below. For testing purposes.          
s1 = '51234'
dll1 = DoublyLinkedNumber()
dll1.tolinkednumber(s1)

s2 = '5'
dll2 = DoublyLinkedNumber()
dll2.tolinkednumber(s2)

print(dll1, "+", dll2, "=", sumlinkednumbers(dll1, dll2))
