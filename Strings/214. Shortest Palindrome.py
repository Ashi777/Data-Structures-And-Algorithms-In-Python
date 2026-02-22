class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return s
        rev_s=s[::-1]
        combined=s+"#"+rev_s
        lps=self.buildLPS(combined)
        longest_prefix=lps[-1]
        return rev_s[:len(s)-longest_prefix]+s

    def buildLPS(self, pattern):
        lps=[0]*len(pattern)
        length=0; i=1
        while i<len(pattern):
            if pattern[i]==pattern[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
        return lps

