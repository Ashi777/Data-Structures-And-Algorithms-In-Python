class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        s="1"
        for _ in range(2, n+1):
            new_s=[]; count=1
            for i in range(1, len(s)):
                if s[i]==s[i-1]:
                    count+=1
                else:
                    new_s.append(str(count))
                    new_s.append(s[i-1])
                    count=1
            new_s.append(str(count))
            new_s.append(s[-1])
            s="".join(new_s)
        return s