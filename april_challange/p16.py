class Solution:
    def remPairs(self, s):
        rem = []
        stack = []
        for c in s:
            if c == ')':
                if not len(stack):
                    rem.append(')')
                else:
                    stack.pop()
            else:
                stack.append('(')
        return rem + stack

    def checkParity(self, parts, frm):
        s = 0 if frm == '(' else len(parts)-1
        e = len(parts) if frm == '(' else -1
        inc = 1 if frm == '(' else -1

        cnt = [[], []]
        for i in range(s, e, inc):
            if parts[i] == 'x':
                continue
            if parts[i] == frm:
                cnt[0].append(i)
            elif parts[i] == '*':
                cnt[1].append(i)
            else:
                if len(cnt[0]) > 0:
                    parts[i] = 'x'
                    parts[cnt[0][-1]] = 'x'
                    cnt[0].pop()
                elif len(cnt[1]) > 0:
                    parts[i] = 'x'
                    parts[cnt[1][-1]] = 'x'
                    cnt[1].pop()
                else:
                    return False
        return True

    def checkValidString(self, s: str) -> bool:
        parts = []
        curr = ''
        for c in s:
            if c == '*':
                parts.append(curr)
                parts.append('*')
                curr = ''
            else:
                curr += c
        if len(curr):
            parts.append(curr)

        sparts = []
        for i in range(len(parts)):
            if parts[i] != '*':
                parts[i] = sparts.extend(self.remPairs(parts[i]))
            else:
                parts[i] = sparts.append('*')
        return self.checkParity(sparts, '(') and self.checkParity(sparts, ')')


s = Solution()
# print(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
# print(s.checkValidString(")("))
print(s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))