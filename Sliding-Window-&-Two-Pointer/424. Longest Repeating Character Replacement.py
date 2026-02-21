class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0; r=0; maxlen=0; maxf=0
        hash=[0]*26
        while(r<len(s)):
            hash[ord(s[r])-ord('A')]+=1
            maxf=max(maxf, hash[ord(s[r])-ord('A')])
            if ((r-l+1)-maxf>k):
                hash[ord(s[l])-ord('A')]-=1
                maxf=0
                l+=1
            if ((r-l+1)-maxf<=k):
                maxlen=max(maxlen, r-l+1)
            r+=1
        return maxlen

