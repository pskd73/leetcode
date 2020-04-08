class Solution:
    def reverse(self, x: int) -> int:
        pos_int = abs(x)
        n = len(str(pos_int))
        rev_int = 0
        i = 1
        
        while pos_int > 0:
            d = pos_int % 10
            pos_int = pos_int // 10
            rev_int += (d * 10**(n - i))
            i += 1
        
        if x < 0:
            rev_int *= -1
            
        if rev_int < -2**31 or rev_int >= 2**31:
            return 0
            
        return rev_int