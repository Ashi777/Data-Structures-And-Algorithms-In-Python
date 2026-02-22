class Solution:
    def search(self, pat, txt):
        n=len(txt); m=len(pat); res=[]
        if m==0: return 0
        for i in range(n-m+1):
            if txt[i:i+m]==pat:
                res.append(i)
        return res

