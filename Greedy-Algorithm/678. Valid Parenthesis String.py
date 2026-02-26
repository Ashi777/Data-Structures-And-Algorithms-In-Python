class Solution:
    def checkValidString(self, s: str) -> bool:
        mins=0; maxs=0; n = len(s)
        for i in range(n):
            if(s[i]=="("):
                mins+=1
                maxs+=1
            elif(s[i]==")"):
                mins-=1
                maxs-=1
            else:
                mins-=1
                maxs+=1
            if(mins<0): mins=0
            if(maxs<0): return False
        return mins==0

# Driver Code
s = "()"
sol=Solution()
ans=sol.checkValidString(s)
print(ans)

# TC -> O(N)
# SC -> O(1)