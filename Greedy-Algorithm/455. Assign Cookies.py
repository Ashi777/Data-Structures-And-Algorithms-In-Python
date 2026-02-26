class Solution:
    def findContentChildren(self, g, s):
        l = 0  # pointer for Student
        r = 0  # pointer for Cookie
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        while l < n and r < m:
            if g[l] <= s[r]:
                l += 1  # assign cookie to student
            r += 1  # move to the next cookie
        return l


# Driver Code
g = [1,2,3]
s = [1,1]
sol=Solution()
ans=sol.findContentChildren(g, s)
print(ans)

# TC -> O(nlogn + mlogm + m)
# SC -> O(1)