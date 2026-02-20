class Solution:
    def NthRoot(self, n, m):
        low = 1;
        high = m
        while (low <= high):
            mid = (low + high) // 2
            val = self.func(mid, n)
            if (val == m):
                return mid
            elif (val < m):
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def func(self, mid, n):
        ans = 1
        for i in range(n):
            ans = ans * mid
            if ans > 1e18: break
        return ans

# Driver Code
N = 3
M = 27
sol=Solution()
ans=sol.NthRoot(N, M)
print(ans)

# TC -> O(log(base2)N) * O(log(base2)M)
# SC -> O(1)