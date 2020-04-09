class Solution:
    def getNext(self, s, i):
        dels = 0
        while i >= 0:
            if s[i] == '#':
                dels += 1
            else:
                if dels > 0:
                    dels -= 1
                else:
                    return s[i], i
            i -= 1
        return None, -1
        
    def backspaceCompare(self, S: str, T: str) -> bool:
        i1, i2 = len(S)-1, len(T)-1
        while i1 >= 0 and i2 >= 0:
            c1, ti1 = self.getNext(S, i1)
            c2, ti2 = self.getNext(T, i2)
            if c1 != c2:
                return False
            i1 = ti1-1
            i2 = ti2-1
        if self.getNext(S, i1) != self.getNext(T, i2):
            return False
        return True