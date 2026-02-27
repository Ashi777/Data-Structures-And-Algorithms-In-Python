class Solution:
    def solve(self, bt):
        #your code goes here
        bt.sort()
        t=0; wt=0
        for i in range(len(bt)):
            wt+=t
            t+=bt[i]
        return int(wt/len(bt)) if bt else 0

# Driver Code
bt = [4, 1, 3, 7, 2]
sol=Solution()
ans=sol.solve(bt)
print(ans)

# TC -> O(N + NlogN)
# SC -> O(1)