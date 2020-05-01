class Solution:
    def toBinList(self, n):
        return [int(x) for x in list("{0:b}".format(n))]
    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mbin = self.toBinList(m)
        nbin = self.toBinList(n)
        ans, ith, gap = 0, 2**(len(mbin)-1), len(nbin) - len(mbin)
        for i in range(len(mbin)):
            if mbin[i] == 1 and nbin[i+gap] == 1:
                if n-m <= ith:
                    ans += ith
            ith //= 2
        return ans