class Solution:
    def isNum(self, c):
        return (ord(c) >= 48 and ord(c) <= 57)
    
    def myAtoi(self, str: str) -> int:
        from_i = 0
        is_neg = False
        for c in str:
            if c == ' ':
                from_i += 1
            else:
                break

        if from_i < len(str)-1:
            if str[from_i] == '-':
                is_neg = True
                from_i += 1
            elif str[from_i] == '+':
                from_i += 1
            
    
        end_i = from_i
        while end_i < len(str) and self.isNum(str[end_i]):
            end_i += 1
        
        str_num = ''
        for i in range(from_i, end_i):
            str_num += str[i]
            
        if str_num == '':
            return 0
        
        num = int(str_num)
            
        if num < -2**31 or num > 2**31 - 1:
            if is_neg:
                return -1 * 2**31
            return 2**31 - 1
        else:
            if is_neg:
                return -1 * num
            return num


s = Solution()
print(s.myAtoi("  0000000000012345678"))