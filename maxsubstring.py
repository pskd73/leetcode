def lengthOfLongestSubstring(s: str) -> int:
        ss_lens = []
        cs = []
        csm = {}
        for i, c in enumerate(s):
            ind = csm.get(c)
            if ind:
                ss_lens.append(len(cs))
                for i in range(ind):
                    
                cs = cs[1:]
            else:
                cs.append(c)
                csm[c] = i
        if len(cs):
            substrings.append(cs)
        mi = 0
        ml = 0
        print(substrings)
        for i, ss in enumerate(substrings):
            if len(ss) > ml:
                ml = len(ss)
                mi = 0
        return ml


print(lengthOfLongestSubstring('pwwkew'))