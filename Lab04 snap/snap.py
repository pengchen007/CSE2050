import random
class ListNode:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link
        
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None: self._tail = self._head
        self._length += 1

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None: self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link is not self._tail:
                currentnode = currentnode.link

            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
            return item

    def __len__(self):
        return self._length

    def display(self):
        item = self._head
        while item:
            print(item.data, end = " ")
            item = item.link
        print() 

    def alldata(self):
        L = []
        cur = self._head
        while cur is not None:
            L.append(cur.data)
            cur = cur.link
        return L

class LinkedDeque:
    def __init__(self):
        self._L = LinkedList()

    def addfirst(self, item):
        self._L.addfirst(item)

    def removefirst(self):
        return self._L.removefirst()

    def addlast(self, item):
        self._L.addlast(item)

    def removelast(self):
        return self._L.removelast()

    def __len__(self):
        return len(self._L)

    def display(self):
        self._L.display()

    def alldata(self):
        return self._L.alldata()

def displaydeck(deck):
    for card in deck:
        print(card, end = ' ')
    print()

def playgame(seed):
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
    random.seed(seed)
    random.shuffle(deck)
    deckA = deck[:26]
    deckB = deck[26:]
    deck_a = LinkedDeque()
    for i in deckA:
        deck_a.addlast(i)
    deck_b = LinkedDeque()
    for i in deckB:
        deck_b.addlast(i)
    deckP = []
    while len(deck_a)>0 and len(deck_b)>0:
        rand = random.random()
        if rand > 0.5:
            card_a = deck_a.removelast()
        else:
            card_a = deck_a.removefirst()
        if card_a in deckP:
            idx = deckP.index(card_a)
            deckP.append(card_a)
            pick_up = deckP[idx:]
            for i in pick_up:
                deck_a.addlast(i)
            deckP = deckP[:idx]
        else:
            deckP.append(card_a)
        if len(deck_a) == 0:
            return ("B wins", deck_b.alldata())
        rand = random.random()
        if rand > 0.5:
            card_b = deck_b.removelast()
        else:
            card_b = deck_b.removefirst()
        if card_b in deckP:
            idx = deckP.index(card_b)
            deckP.append(card_b)
            pick_up = deckP[idx:]
            for i in pick_up:
                deck_b.addlast(i)
            deckP = deckP[:idx]
        else:
            deckP.append(card_b)    
        if len(deck_b) == 0:
            return ("A wins", deck_a.alldata())


print(playgame(305))
print(playgame(100))
print(playgame(200))
print(playgame(300))
print(playgame(400))
print(playgame(1200))
print(playgame(1250))
print(playgame(1350))
print(playgame(1))
print(playgame(6))
print(playgame(11))
print(playgame(16))
print(playgame(21))


