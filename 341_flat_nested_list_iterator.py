class NestedInteger:
    def __init__(self, v):
        self.v = v

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return type(self.v) is int

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if self.isInteger():
            return self.v
        return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """    
        if not self.isInteger():
            return self.v
        return None


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [(nestedList, 0)] if len(nestedList) else []
        self.nextEl = self.getNext()

    def next(self) -> int:
        currentEl = self.nextEl
        self.nextEl = self.getNext()
        return currentEl
    
    def getNext(self) -> int:
        if not len(self.stack):
            return None

        cL, cIdx = self.stack.pop()
        print('stack top', cL, cIdx)
        if len(cL) is 0:
            return self.getNext()
        cE = cL[cIdx]
        if cE.isInteger():
            if cIdx < len(cL) - 1:
                cIdx += 1
                self.stack.append((cL, cIdx))
            return cE.getInteger()
        else:
            if cIdx < len(cL) - 1:
                cIdx += 1
                self.stack.append((cL, cIdx))
            self.stack.append((cE.getList(), 0))
            return self.getNext()
    
    def hasNext(self) -> bool:
        return self.nextEl is not None


l = [
    NestedInteger([
        NestedInteger(1), 
        NestedInteger(1)
    ]),
    NestedInteger(2),
    NestedInteger([
        NestedInteger(1), 
        NestedInteger(1)
    ])
]

l2 = [NestedInteger([NestedInteger([])])]

l3 = []

l4 = [NestedInteger([]), NestedInteger([NestedInteger(3)])]

it = NestedIterator(l4)

while it.hasNext():
    print('inside', it.next())